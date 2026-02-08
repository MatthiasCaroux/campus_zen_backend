"""
Middleware d'authentification par cookies HttpOnly pour JWT
"""


class JWTCookieAuthenticationMiddleware:
    """
    Middleware qui extrait le token JWT du cookie HttpOnly et le place
    dans le header Authorization pour l'authentification JWT.
    
    Cela permet aux clients web d'utiliser des cookies HttpOnly sécurisés
    au lieu de stocker les tokens dans localStorage/sessionStorage.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extraction du token depuis le cookie access_token
        access_token = request.COOKIES.get('access_token')
        
        # Si un token existe dans le cookie et qu'il n'y a pas déjà
        # un header Authorization, on l'ajoute
        if access_token and not request.META.get('HTTP_AUTHORIZATION'):
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
        
        response = self.get_response(request)
        return response

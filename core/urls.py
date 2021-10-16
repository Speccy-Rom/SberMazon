from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "cart/",
        include(
            "cart.urls",
        ),
    ),
    path(
        "",
        include(
            "shop.urls",
        ),
    ),
]

if settings.DEBUG:
    # import debug_toolbar  # noqa

    # urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

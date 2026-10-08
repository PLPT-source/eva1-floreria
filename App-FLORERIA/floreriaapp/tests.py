from django.test import TestCase
from django.urls import reverse
from .models import Producto

OK = dict(nombre='Ramo rosas', precio=15000, stock=5)


class CrudTests(TestCase):
    def test_crud_completo(self):
        self.client.post(reverse('crear_producto'), OK)
        p = Producto.objects.get()
        self.assertEqual(self.client.get(reverse('listar_productos')).status_code, 200)
        self.client.post(reverse('editar_producto', args=[p.id]), {**OK, 'precio': 20000, 'disponible': 'on'})
        p.refresh_from_db(); self.assertEqual(p.precio, 20000)
        self.client.post(reverse('eliminar_producto', args=[p.id]))
        self.assertEqual(Producto.objects.count(), 0)

    def test_validaciones(self):
        for malo in ({'precio': 0}, {'stock': -1}, {'proveedor_email': 'x'}, {'nombre': ''}):
            self.client.post(reverse('crear_producto'), {**OK, **malo})
        self.assertEqual(Producto.objects.count(), 0)

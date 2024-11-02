import django.shortcuts
import django.test


class FormTest(django.test.TestCase):
    def test_context(self):
        url = django.shortcuts.reverse("feedback:feedback")
        response = django.test.Client().get(url)
        self.assertIn("form", response.context)

    def test_labels(self):
        url = django.shortcuts.reverse("feedback:feedback")
        response = django.test.Client().get(url)
        self.assertEqual(response.context["form"]["name"].label, "Имя")
        self.assertEqual(response.context["form"]["text"].label, "Фидбек")
        self.assertEqual(response.context["form"]["mail"].label, "Email")

    def test_help_texts(self):
        url = django.shortcuts.reverse("feedback:feedback")
        response = django.test.Client().get(url)
        self.assertEqual(response.context["form"]["name"].help_text, "Имя")
        self.assertEqual(response.context["form"]["text"].help_text, "Фидбек")
        self.assertEqual(response.context["form"]["mail"].help_text, "Email")

    def test_redirect(self):
        url = django.shortcuts.reverse("feedback:feedback")
        response = self.client.post(
            url,
            data={"name": "123", "text": "123", "mail": "123@123.123"},
        )
        self.assertRedirects(response, url)


__all__ = ()

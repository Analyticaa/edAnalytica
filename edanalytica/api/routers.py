from rest_framework import routers
from api.views import QuestionViewset, SubmissionViewset

router = routers.DefaultRouter()
router.register(r'question', QuestionViewset)
router.register(r'submission', SubmissionViewset)
urlpatterns = router.urls
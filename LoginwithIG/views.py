import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def ProfileDataView(req, format=None):
    data = {}

    instaaccesstokenreq = requests.post(
        "https://api.instagram.com/oauth/access_token?client_id=1776611746023170&client_secret=e4e0ce95bf57d067a1668b2b4ae602e6&grant_type=authorization_code&redirect_uri=https://connecttoinstaaccount.netlify.app&code=" + req.data.code)
    instaaccesstoken = instaaccesstokenreq.json()

    instadatareq = requests.get(
        "https://graph.instagram.com/me/media?fields=id,username,media_type,media_url,caption,permalink&access_token="+instaaccesstoken["access_token"])

    instadata = instadatareq.json()

    data["user_id"] = instaaccesstoken["user_id"]
    data["access_token"] = "IGQVJXLWl1MjkzQWdGNUs2amxjbFVVRTRVdjg4a25TRkVneXhJazVrVUM1dVRBNjRlSVYxSEVhSmxlM1l5LU9hN2cwQWtvQVZA2S08wMVhiS3E5TTg0cHhSQThuX1RvNUdhZAlNVeUhPb0xFU0ptVUE5TQZDZD"
    data["data"] = instadata["data"]

    return Response(data)

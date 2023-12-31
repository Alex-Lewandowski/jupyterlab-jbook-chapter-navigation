import json


async def test_get_example(jp_fetch):
    # When
    response = await jp_fetch("jlab-jbook-chapter-navigation", "get-toc")

    # Then
    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "data": "This is /jlab-jbook-chapter-navigation/get-toc endpoint!"
    }
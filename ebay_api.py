def search_ebay(keywords):
    # This is a mock function that returns fake data
    mock_items = [
        {
            "id": 1,
            "name": f"Mock Product 1 for {keywords}",
            "price": "$19.99",
            "image": "https://via.placeholder.com/150",
            "url": "https://www.ebay.com/sch/i.html?_nkw=" + keywords.replace(" ", "+")
        },
        {
            "id": 2,
            "name": f"Mock Product 2 for {keywords}",
            "price": "$24.99",
            "image": "https://via.placeholder.com/150",
            "url": "https://www.ebay.com/sch/i.html?_nkw=" + keywords.replace(" ", "+")
        },
        {
            "id": 3,
            "name": f"Mock Product 3 for {keywords}",
            "price": "$14.99",
            "image": "https://via.placeholder.com/150",
            "url": "https://www.ebay.com/sch/i.html?_nkw=" + keywords.replace(" ", "+")
        }
    ]
    return mock_items
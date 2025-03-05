import requests
url = "https://www.google.com/search?tbm=map&pb=!4m12!1m3!1d2785268.999120552!2d-75.35320564999998!3d41.860978072031365!2m3!1f0!2f0!3f0!3m2!1i1038!2i703!4f13.1!7i20!10b1!12m22!1m3!18b1!30b1!34e1!2m3!5m1!6e2!20e3!4b0!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!46m1!1b0!96b1!19m4!2m3!1i360!2i120!4i8!20m48!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m33!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!1m3!1e9!2b1!3e2!2b1!9b0!22m2!1sPK-rZ_DDA6eJptQPn_qU8A4!7e81!24m108!1m32!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m21!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!17b1!20b1!21b1!22b1!25b1!27m1!1b0!28b0!32b1!33m1!1b1!34b0!36e1!10m1!8e3!11m1!3e1!14m1!3b0!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m1!1b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m22!1m8!2b1!5b1!7b1!12m4!1b1!2b1!4m1!1e1!4b1!8m10!1m6!4m1!1e1!4m1!1e3!4m1!1e4!3sother_user_google_reviews!6m1!1e1!9b1!89b1!98m3!1b1!2b1!3b1!103b1!113b1!114m3!1b1!2m1!1b1!117b1!122m1!1b1!125b0!126b1!127b1!26m4!2m3!1i80!2i92!4i8!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!47m0!49m10!3b1!6m2!1b1!2b1!7m2!1e3!2b1!8b1!9b1!10e2!61b1!62b1!67m3!7b1!10b1!14b1!69i720!72m2!1m1!1s0x89c259a40fe9c287%3A0xab59c64d4273d41f!72m2!1m1!1s0x89c259dbd763011d%3A0x64cf6616c725b564!72m2!1m1!1s0x89c259a665325aff%3A0x3ac777522187cfd5!72m2!1m1!1s0x89c259a67765432b%3A0xb69ca2cc7e7de7c8!72m2!1m1!1s0x89c2598590a04521%3A0x7d853708fe697388!72m2!1m1!1s0x89c259b0680d0eb1%3A0x4ccadb59adb69b85!72m2!1m1!1s0x89c259131b6acc25%3A0x9b5580f8ae2d380!72m2!1m1!1s0x89c2585611387a67%3A0xbb14b5d816af777f!72m2!1m1!1s0x89c25931b54e99f9%3A0xf541ad5f51dcaaaa!72m2!1m1!1s0x89c259a774293ced%3A0xd3dc33bf737db256!72m2!1m1!1s0x89c259ab3c1ef289%3A0x3b67a41175949f55!72m2!1m1!1s0x89c25999d8fc75d3%3A0x49568ef034f85779!72m2!1m1!1s0x89c25920f907ac49%3A0xe842fc3f42af7c20!72m2!1m1!1s0x89c25855c88f3fcf%3A0x5b626ea7d0739ec2!72m2!1m1!1s0x89c259d17ff9b36f%3A0x5b2e038274ac74d8!72m2!1m1!1s0x89c25854e6657b87%3A0xed0e40a6b9508db5!72m2!1m1!1s0x89c25854e6657b87%3A0x1627fdc289dd3acf!72m2!1m1!1s0x89c25854d7f642fd%3A0x92c6f656266909f!72m2!1m1!1s0x89c259acc56ff1cf%3A0x42673d7fc58eb102!72m2!1m1!1s0x89c259acb066092b%3A0x360f6fb2c6eab47c&q=*"
headers = {"Referer": "https://www.google.com/"}

def fetch_stops_from_maps():
    new_results = -1
    page = 0
    results = []

    while new_results != 0:
        new_results = 0
        x = requests.get(url % page, headers=headers)
        txt = html.unescape(x.text)
        txt = txt.split("\n")[1]
        results = re.findall(r"\[null,null,[0-9]{1,2}\.[0-9]{4,15},[0-9]{1,2}\.[0-9]{4,15}]", txt)

        print(len(results))
        for cord in results:
            # curr = the description you can manually type in when saving
            curr = txt.split(cord)[1].split("\"]]")[0]
            curr = curr[curr.rindex(",\"") + 2:]

            cords = str(cord).split(",")
            lat = cords[2]
            lon = cords[3][:-1]

            results.append(s)
            new_results += 1
        page += 2

fetch_stops_from_maps()
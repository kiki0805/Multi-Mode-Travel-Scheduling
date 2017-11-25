    #-*- coding:utf-8 –*-
def recommend(key_user_tag):
    # Input key user info.
    #key_user_tag = set(['KTV','桌游店','游乐场','体育场','体育馆']);

    # Initialize counting bin for tags.
    counting_bin = {'KTV': 0, '桌游店': 0, '电影院': 0, '游乐场': 0, '体育场': 0, '体育馆': 0, '网球场': 0, '足球场': 0, '篮球场': 0, '游泳馆': 0, '乒乓球馆': 0, '羽毛球场': 0, '蹦极': 0, '西餐厅': 0, '中餐': 0, '日料': 0, '快餐': 0, '星级景点': 0, '保护建筑': 0, '网吧': 0, '台球房': 0, '击剑馆': 0, '保龄球馆': 0, '酒吧': 0, '剧院': 0, '音乐厅': 0, '图书馆': 0, '博物馆': 0, '会所': 0, '公园': 0};

    # Input database.
    file = open("database.txt")
    database = []
    while 1:
        line = file.readline()
        if not line:
            break
        database.append(line)

    # KNN.
    for i in range(len(database)):
        # Read user info.
        tags = []
        temp = database[i].split('[');
        temp = temp[1].split(']');
        temp = temp[0].split(',');
        for j in range(5):
            temp_tag = temp[j].split(": '");
            temp_tag = temp_tag[1].split("'");
            tags.append(temp_tag[0]);
        # Find the similarity between two.
        temp_set = key_user_tag&set(tags);
        # If the difference is larger than threshold (3 in 5), ignore.
        if (len(temp_set) < 3):
            continue;
        # Add this users other tag into counting bin.
        for k in range(5):
            if (tags[k] not in key_user_tag):
                counting_bin[tags[k]] += 1;

    # Output top 5 recommended tag.
    output = [];
    for i in range(5):
        output_tag = sorted(counting_bin,key=lambda x:counting_bin[x])[-1];
        del counting_bin[output_tag];
        output.append(output_tag);
        print(output_tag)
    
    return output
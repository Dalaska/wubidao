"""
Wubidao — 五笔道
--------------------------------
An interactive Wubi typing practice game.
Author: zdr 
"""

from __future__ import annotations

COMMON_WORD_MAP: Dict[Word, Code] = {'老师': 'fxjg', '学生': 'iptg', '同学': 'mgip', '同事': 'mggk', '朋友': 'eedc', '家长': 'peta', '父母': 'wqxg', '孩子': 'bybb', '男人': 'llww', '女人': 'vvww', '大人': 'ddww', '小孩': 'ihby', '邻居': 'wynd', '客人': 'ptww', '主人': 'ygww', '领导': 'wynf', '上司': 'hhng', '下属': 'ghnt', '伙伴': 'wowu', '记者': 'ynfj', '医生': 'attg', '护士': 'ryfg', '病人': 'ugww', '店员': 'yhkm', '顾客': 'dbpt', '司机': 'ngsm', '售货': 'wowx', '警察': 'aqpw', '农民': 'pena', '工人': 'aaww', '老板': 'fxsr', '室友': 'pgdc', '校长': 'suta', '同乡': 'mgxt', '作者': 'wtfj', '读者': 'yffj', '经理': 'xcgj', '同志': 'mgfn', '老友': 'fxdc', '亲友': 'usdc', '今天': 'wygd', '明天': 'jegd', '昨天': 'jtgd', '现在': 'gmdh', '时候': 'jfwh', '当时': 'ivjf', '今年': 'wyrh', '去年': 'fcrh', '明年': 'jerh', '本周': 'sgmf', '上周': 'hhmf', '下周': 'ghmf', '上午': 'hhtf', '下午': 'ghtf', '早上': 'jhhh', '中午': 'khtf', '晚上': 'jqhh', '夜里': 'ywjf', '午夜': 'tfyw', '早晨': 'jhjd', '傍晚': 'wujq', '黄昏': 'amqa', '周末': 'mfgs', '假期': 'wnad', '假日': 'wnjj', '春天': 'dwgd', '夏天': 'dhgd', '秋天': 'togd', '冬天': 'tugd', '近日': 'rpjj', '学校': 'ipsu', '公司': 'wcng', '医院': 'atbp', '银行': 'qvtf', '超市': 'fhym', '商店': 'umyh', '饭店': 'qnyh', '餐厅': 'hqds', '车站': 'lguh', '机场': 'smfn', '地铁': 'fbqr', '公园': 'wclf', '书店': 'nnyh', '旅馆': 'otqn', '宾馆': 'prqn', '酒店': 'isyh', '宿舍': 'pwwf', '厂房': 'dgyn', '会场': 'wffn', '球场': 'gffn', '剧院': 'ndbp', '广场': 'yyfn', '市场': 'ymfn', '菜场': 'aefn', '商场': 'umfn', '码头': 'dcud', '海边': 'itlp', '河边': 'islp', '湖边': 'idlp', '山区': 'mmaq', '市区': 'ymaq', '郊区': 'uqaq', '小区': 'ihaq', '城区': 'fdaq', '乡村': 'xtsf', '农村': 'pesf', '大学': 'ddip', '中学': 'khip', '小学': 'ihip', '影院': 'jybp', '书房': 'nnyn', '厨房': 'dgyn', '客厅': 'ptds', '卧室': 'ahpg', '阳台': 'bjck', '厕所': 'dmrn', '院子': 'bpbb', '门口': 'uykk', '路口': 'ltkk', '身体': 'tmws', '头发': 'udnt', '眼睛': 'hvhg', '耳朵': 'bgms', '鼻子': 'thbb', '嘴巴': 'khcn', '牙齿': 'ahhw', '舌头': 'tdud', '手指': 'rtrx', '手臂': 'rtnk', '胳膊': 'eteg', '肩膀': 'yneu', '背部': 'uxuk', '胸口': 'eqkk', '腰部': 'esuk', '大腿': 'ddev', '小腿': 'ihev', '脚趾': 'eflh', '脚跟': 'eflv', '脚底': 'efyq', '皮肤': 'hcef', '心脏': 'nyey', '头痛': 'uduc', '发烧': 'ntoa', '感冒': 'dgjh', '咳嗽': 'kykg', '药店': 'axyh', '药房': 'axyn', '急诊': 'qvyw', '手术': 'rtsy', '学习': 'ipnu', '工作': 'aawt', '生活': 'tgit', '阅读': 'uuyf', '写作': 'pgwt', '思考': 'lnfg', '讨论': 'yfyw', '决定': 'unpg', '选择': 'rqrc', '计划': 'yfaj', '组织': 'xexk', '安排': 'pvrj', '准备': 'uwtl', '参加': 'cdlk', '支持': 'fcrf', '帮助': 'dteg', '保护': 'wkry', '发展': 'ntna', '加强': 'lkxk', '改变': 'ntyo', '改进': 'ntfj', '提高': 'rjym', '降低': 'btwq', '增加': 'fulk', '减少': 'udit', '购买': 'mqnu', '销售': 'qiwo', '出发': 'bmnt', '到达': 'gcdp', '通过': 'cefp', '进入': 'fjty', '离开': 'ybga', '打开': 'rsga', '关闭': 'uduf', '使用': 'wgeh', '操作': 'rkwt', '保存': 'wkdh', '删除': 'mmbw', '更新': 'gjus', '上传': 'hhwf', '下载': 'ghfa', '登录': 'ogvi', '注册': 'iymm', '复习': 'tjnu', '预习': 'cnnu', '退货': 'vewx', '理财': 'gjmf', '购物': 'mqrh', '点餐': 'hkhq', '打车': 'rslg', '乘车': 'tulg', '换乘': 'rqtu', '上班': 'hhgy', '下班': 'ghgy', '请假': 'ygwn', '加班': 'lkgy', '出差': 'bmud', '付款': 'wfff', '收款': 'nhff', '手机': 'rtsm', '电脑': 'jney', '网络': 'mqxt', '网站': 'mquh', '软件': 'lqwr', '硬件': 'dgwr', '程序': 'tkyc', '数据': 'ovrn', '模型': 'saga', '训练': 'ykxa', '算法': 'thif', '代码': 'wadc', '调试': 'ymya', '测试': 'imya', '部署': 'uklf', '云端': 'fcum', '云盘': 'fcte', '邮件': 'mbwr', '短信': 'tdwy', '通话': 'ceyt', '拍照': 'rrjv', '视频': 'pyhi', '音频': 'ujhi', '账号': 'mtkg', '密码': 'pndc', '车辆': 'lglg', '公交': 'wcuq', '火车': 'oolg', '高铁': 'ymqr', '飞机': 'nusm', '骑行': 'cdtf', '驾车': 'lklg', '停车': 'wylg', '车票': 'lgsf', '机票': 'smsf', '航班': 'tegy', '站台': 'uhck', '轨道': 'lvut', '航站': 'teuh', '船票': 'tesf', '公路': 'wclt', '高速': 'ymgk', '事故': 'gkdt', '堵车': 'fflg', '路况': 'ltuk', '导航': 'nfte', '油价': 'imww', '加油': 'lkim', '充电': 'ycjn', '车位': 'lgwu', '车主': 'lgyg', '车厢': 'lgds', '路段': 'ltwd', '饭菜': 'qnae', '米饭': 'oyqn', '面条': 'dmts', '包子': 'qnbb', '饺子': 'qnbb', '馒头': 'qnud', '稀饭': 'tqqn', '水果': 'iijs', '蔬菜': 'anae', '苹果': 'agjs', '香蕉': 'tjaw', '橙子': 'sobb', '葡萄': 'aqaq', '草莓': 'ajat', '西瓜': 'sgrc', '咖啡': 'klkj', '茶叶': 'awkf', '牛奶': 'rhve', '豆浆': 'gkuq', '啤酒': 'kris', '白酒': 'rris', '红酒': 'xais', '酸奶': 'sgve', '酱油': 'uqim', '辣椒': 'udsh', '猪肉': 'efmw', '牛肉': 'rhmw', '羊肉': 'udmw', '鸡蛋': 'cqnh', '菜油': 'aeim', '教室': 'fbpg', '课本': 'yjsg', '课文': 'yjyy', '作业': 'wtog', '考试': 'fgya', '成绩': 'dnxg', '分数': 'wvov', '题目': 'jghh', '教师': 'fbjg', '学员': 'ipkm', '校友': 'sudc', '校园': 'sulf', '学期': 'ipad', '学费': 'ipxj', '专业': 'fnog', '研究': 'dgpw', '毕业': 'xxog', '学位': 'ipwu', '论文': 'ywyy', '讲座': 'yfyw', '作文': 'wtyy', '语法': 'ygif', '词汇': 'ynia', '发音': 'ntuj', '课堂': 'yjip', '家庭': 'peyt', '家人': 'peww', '房子': 'ynbb', '房间': 'ynuj', '厨具': 'dghw', '家具': 'pehw', '沙发': 'iint', '桌子': 'hjbb', '椅子': 'sdbb', '灯光': 'osiq', '电灯': 'jnos', '电器': 'jnkk', '冰箱': 'uits', '电视': 'jnpy', '空调': 'pwym', '洗衣': 'irye', '拖地': 'rtfb', '扫地': 'rvfb', '叠衣': 'ccye', '晾衣': 'jyye', '被子': 'pubb', '枕头': 'spud', '毛巾': 'tfmh', '牙刷': 'ahnm', '牙膏': 'ahyp', '纸巾': 'xqmh', '拖鞋': 'rtak', '雨伞': 'kgwu', '餐具': 'hqhw', '炊具': 'oqhw', '天气': 'gdrn', '气温': 'rnij', '气候': 'rnwh', '多云': 'qqfc', '晴天': 'jggd', '阴天': 'begd', '小雨': 'ihkg', '大雨': 'ddkg', '暴雨': 'jakg', '大雪': 'ddkv', '小雪': 'ihkv', '台风': 'ckmq', '彩虹': 'esja', '露水': 'klii', '海洋': 'itiu', '森林': 'ssss', '山脉': 'mmey', '河流': 'isiy', '湖泊': 'idir', '沙漠': 'iiia', '政治': 'ghic', '经济': 'xciy', '社会': 'pywf', '文化': 'yywx', '历史': 'dlkq', '法律': 'iftv', '教育': 'fbyc', '医疗': 'atub', '科技': 'turf', '贸易': 'qyjq', '金融': 'qqgk', '税收': 'tunh', '贷款': 'waff', '汇率': 'iayx', '通胀': 'ceet', '就业': 'yiog', '创业': 'wbog', '企业': 'whog', '产业': 'utog', '部门': 'ukuy', '政策': 'ghtg', '规定': 'fwpg', '标准': 'sfuw', '安全': 'pvwg', '风险': 'mqbw', '责任': 'gmwt', '权利': 'sctj', '权益': 'scuw', '民生': 'natg', '环保': 'gdwk', '足球': 'lhgf', '篮球': 'tjgf', '网球': 'mqgf', '排球': 'rjgf', '乒乓': 'rgrg', '游泳': 'ioiy', '跑步': 'lqhi', '健身': 'wvtm', '瑜伽': 'gwwl', '摄影': 'rbjy', '旅游': 'otio', '音乐': 'ujqi', '电影': 'jnjy', '绘画': 'xwgl', '书法': 'nnif', '舞蹈': 'rlle', '游戏': 'ioca', '下棋': 'ghsa', '钓鱼': 'qqpt', '露营': 'klap', '红色': 'xaqc', '蓝色': 'ajqc', '绿色': 'xvqc', '黄色': 'amqc', '黑色': 'lfqc', '白色': 'rrqc', '紫色': 'hxqc', '橙色': 'soqc', '灰色': 'doqc', '棕色': 'spqc', '银色': 'qvqc', '金色': 'qqqc', '圆形': 'lkga', '方形': 'oyga', '三角': 'dgqe', '长方': 'taoy', '正方': 'ghoy', '椭圆': 'sblk', '线条': 'xfts', '图形': 'ltga', '因为': 'ldyl', '所以': 'rnny', '如果': 'vkjs', '还是': 'dpjg', '但是': 'wjjg', '然后': 'qdrg', '而且': 'dmeg', '以及': 'nyey', '并且': 'uaeg', '或者': 'akfj', '还有': 'dpe', '已经': 'nnxc', '一直': 'ggfh', '终于': 'xtsg', '突然': 'pwqd', '马上': 'cnhh', '立即': 'uuvc', '大概': 'ddsv', '也许': 'bnyt', '可能': 'skce', '国家': 'lgpe', '地区': 'fbaq', '城市': 'fdym', '乡镇': 'xtqf', '村庄': 'sfyf', '社区': 'pyaq', '人口': 'wwkk', '居民': 'ndna', '亲属': 'usnt', '夫妻': 'fwgv', '关系': 'udtx', '问题': 'ukjg', '答案': 'twpv', '方法': 'oyif', '结果': 'xfjs', '效果': 'uqjs', '水平': 'iigu', '能力': 'celn', '经验': 'xccw', '习惯': 'nunx', '兴趣': 'iwfh', '爱好': 'epvb', '意见': 'ujmq', '建议': 'vfyy', '方案': 'oypv', '目标': 'hhsf', '任务': 'wttl', '项目': 'adhh', '程度': 'tkya', '范围': 'ailf', '方面': 'oydm', '内容': 'mwpw', '情况': 'nguk', '条件': 'tswr', '环境': 'gdfu', '资源': 'uqid', '信息': 'wyth', '新闻': 'usub', '报道': 'rbut', '媒体': 'vaws', '规范': 'fwai', '指南': 'rxfm', '细则': 'xlmj'}


import json
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple, Any
from wcwidth import wcswidth

# ==========================================
# Config & Types
# ==========================================
Word = str
Code = str
AttemptStats = Tuple[int, int]  # (total_attempts, wrong_attempts)

# ---- Constants ----
PROGRESS_FILE = "wubidao_saved_game.json"
CANDIDATE_LIMIT_DEFAULT = 7
META_KEYS = {"level"}

MIN_ATTEMPTS_TO_PASS = 3
MIN_ACCURACY = 0.60

ADD_NEW: Dict[int, str] = {
    2: 'f', 3: 'w', 4: 'n', 5: 'd', 6: 'u', 7: 'q', 8: 'a', 9: 'i',
    10: 'j', 11: 'm', 12: 's', 13: 'k', 14: 'c', 15: 'p', 16: 'r',
    17: 'e', 18: 'l', 19: 'b', 20: 'x', 21: 'o', 22: 'v', 23: 'z'
}
BASE_KEYS = ['t', 'y', 'g', 'h']



# ==========================================
# JSON Store Utilities
# ==========================================
def load_json(path: Path, default: MutableMapping | None = None) -> MutableMapping:
    if default is None:
        default = {"level": 0}
    if not path.exists():
        return default.copy()
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return default.copy()
        for k, v in default.items():
            data.setdefault(k, v)
        return data
    except Exception:
        return default.copy()


def save_json(path: Path, data: Mapping) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_progress(filename: str = PROGRESS_FILE) -> Dict[str, Any]:
    return dict(load_json(Path(filename)))


def save_progress(
    session_stats: Mapping[Word, AttemptStats],
    progress_file: str = PROGRESS_FILE,
    level: int | None = None,
) -> Dict[str, object]:
    """
    Merge current session stats into persistent progress.
    """
    path = Path(progress_file)
    data: Dict[str, object] = dict(load_json(path))

    for word, (total, wrong) in session_stats.items():
        if word in META_KEYS:
            continue
        prev = data.get(word)
        if isinstance(prev, list) and len(prev) == 2:
            data[word] = [prev[0] + total, prev[1] + wrong]
        else:
            data[word] = [total, wrong]

    if level is not None:
        prev_level = data.get("level", 1)
        if isinstance(prev_level, int):
            data["level"] = max(prev_level, level)
        else:
            data["level"] = level

    save_json(path, data)
    return data


# ==========================================
# Candidate Selection
# ==========================================
def ensure_words_tracked(words: Iterable[Word], store: MutableMapping[str, object]) -> None:
    for w in words:
        if w in META_KEYS:
            continue
        if w not in store or not (isinstance(store[w], list) and len(store[w]) == 2):
            store[w] = [0, 0]


def select_practice_words(
    known_keys: Iterable[str],
    word_map: Mapping[Word, Code],
    progress_file: str = PROGRESS_FILE,
) -> List[Tuple[Word, Code]]:
    """
    Return [(word, code)] where all code letters are in known_keys.
    Sorts by fewest prior attempts first.
    """
    known_set = set(known_keys)
    store = read_progress(progress_file)

    picked: List[Tuple[Word, Code]] = [
        (w, code) for w, code in word_map.items()
        if set(code).issubset(known_set)
    ]

    ensure_words_tracked((w for w, _ in picked), store)

    def sort_key(item: Tuple[Word, Code]) -> int:
        meta = store.get(item[0], [9999, 0])
        return int(meta[0]) if isinstance(meta, list) and meta else 9999

    picked.sort(key=sort_key)
    save_json(Path(progress_file), store)
    return picked


# ==========================================
# Wubi Table Printer
# ==========================================
def print_wubi_table(known_world: Iterable[str], new_block: str | None = None) -> None:
    known_world_set = set(known_world)

    data = {
        "q": ["金勺缺点无尾鱼犬旁留叉氏无七"],
        "w": ["人八登祭取字头"],
        "e": ["月彡乃用家衣底"],
        "r": ["白手看头三二斤"],
        "t": ["禾竹一撇双人反文条头"],
        "y": ["言文方广在四一高头一捺谁人去"],
        "u": ["立辛两点六门病"],
        "i": ["水旁兴头小倒立"],
        "o": ["火业头四点米"],
        "p": ["之宝盖摘示衣"],
        "a": ["工戈草头右框七"],
        "s": ["木丁西"],
        "d": ["大犬三羊古石厂"],
        "f": ["土士二干十寸雨"],
        "g": ["王旁青头戋五一"],
        "h": ["目具上止卜虎皮"],
        "j": ["日早两竖与虫依"],
        "k": ["口与川"],
        "l": ["田甲方框四车力"],
        "x": ["慈母无心弓和匕幼无力"],
        "c": ["又巴马丢矢矣"],
        "v": ["女刀九臼山朝西"],
        "b": ["子耳了也框向上"],
        "n": ["已半巳满不出己左框折尸心和羽"],
        "m": ["山由贝下框几"],
    }
    rows = ["qwertyuiop", "asdfghjkl", "xcvbnm"]

    reset, blue, magenta, green, cyan, red, yellow = (
        "\033[0m", "\033[34m", "\033[35m", "\033[32m", "\033[36m", "\033[31m", "\033[33m"
    )

    group_color = {}
    for k in "qwert": group_color[k] = blue
    for k in "yuiop": group_color[k] = magenta
    for k in "asdfg": group_color[k] = green
    for k in "hjklm": group_color[k] = cyan
    for k in "xcvbn": group_color[k] = red

    def wlen(s: str) -> int:
        w = wcswidth(s)
        return len(s) if w < 0 else w

    def pad_left_cjk(s: str, width: int) -> str:
        s = s or ""
        return s + " " * max(0, width - wlen(s))

    def chunk_by_chars(s: str, n: int) -> list[str]:
        return [s[i:i+n] for i in range(0, len(s), n)] or [""]

    def color_for_key(key: str) -> str:
        return yellow if (new_block and key == new_block) else group_color.get(key, reset)

    def paint(s: str, key: str) -> str:
        return f"{color_for_key(key)}{s}{reset}"

    def make_box(key: str, text: str, show_body: bool) -> list[str]:
        inner_w = 6
        top = "┌" + "─" * inner_w + "┐"
        lab = "│" + pad_left_cjk(key, inner_w) + "│"
        box = [paint(top, key), paint(lab, key)]
        if show_body:
            for seg in chunk_by_chars(text, 3):
                box.append(paint("│" + pad_left_cjk(seg, inner_w) + "│", key))
        box.append(paint("└" + "─" * inner_w + "┘", key))
        return box

    def join_row(keys: str, indent: int = 0) -> str:
        boxes = [make_box(k, data.get(k, [""])[0], k in known_world_set) for k in keys]
        max_h = max(len(b) for b in boxes)
        for i, b in enumerate(boxes):
            if len(b) < max_h:
                key = keys[i]
                empty_line = paint("│" + " " * 6 + "│", key)
                boxes[i] = b[:-1] + [empty_line] * (max_h - len(b)) + [b[-1]]
        return "\n".join((" " * indent) + "".join(b[r] for b in boxes) for r in range(max_h))

    print(join_row(rows[0])); print()
    print(join_row(rows[1])); print()
    print(join_row(rows[2], indent=4))


# ==========================================
# Progress Policy
# ==========================================
def wubidao_progress_policy(stats: Dict[Word, AttemptStats]) -> bool:
    filtered_stats = {k: v for k, v in stats.items() if k not in META_KEYS}
    if not filtered_stats:
        print("No stats available.")
        return False

    print("\n📊 Progress summary:")
    total_words, passed_words = len(filtered_stats), 0
    for word, (total, wrong) in filtered_stats.items():
        accuracy = (total - wrong) / total if total > 0 else 0
        passed = total >= MIN_ATTEMPTS_TO_PASS and accuracy >= MIN_ACCURACY
        status = "✅ Pass" if passed else "🐣 Need work"
        print(f"  {word}: {accuracy*100:.1f}% ({total}/{MIN_ATTEMPTS_TO_PASS} tries, {wrong} wrong) {status}")
        if passed: passed_words += 1

    pass_rate = passed_words / total_words
    print(f"\nOverall pass rate: {pass_rate*100:.1f}% ({passed_words}/{total_words})")
    all_passed = passed_words == total_words
    print("🎉 All words passed! Level up!" if all_passed else "💪 Keep practicing!")
    return all_passed


# ==========================================
# Level Helpers
# ==========================================
def build_level_set(base_keys: Sequence[str], add_new: Mapping[int, str]) -> Dict[int, Tuple[str, ...]]:
    level_set: Dict[int, Tuple[str, ...]] = {1: tuple(base_keys)}
    current = list(base_keys)
    for lvl in range(2, max(add_new.keys()) + 1):
        nk = add_new.get(lvl)
        if nk:
            current.append(nk)
        level_set[lvl] = tuple(current)
    return level_set


def get_keys_for_level(level: int, level_set: Mapping[int, Sequence[str]]) -> Sequence[str]:
    if level in level_set:
        return level_set[level]
    return level_set[max(level_set)]


# ==========================================
# Quiz Loop
# ==========================================
def quiz_loop(
    candidate_words: Sequence[Tuple[Word, Code]],
    known_keys: Iterable[str],
    input_fn: Callable[[str], str] = input,
    print_fn: Callable[[str], None] = print,
) -> Tuple[Dict[Word, AttemptStats], bool]:
    stats: Dict[Word, AttemptStats] = {}
    EXIT = False
    i, n = 0, len(candidate_words)

    while i < n:
        word, code = candidate_words[i]
        user_in = input_fn(f"[{word}]: ").strip()

        if user_in == ":exit":
            EXIT = True
            break
        if user_in == ":show":
            print_wubi_table(known_world=known_keys)
            continue

        total, wrong = stats.get(word, (0, 0))
        if user_in == code:
            stats[word] = (total + 1, wrong)
            print_fn("✅")
            i += 1
        else:
            print_fn("\n" * 40)
            print_fn("😅")
            print_fn(f"\033[33m{word}: {code}\033[0m")
            stats[word] = (total + 1, wrong + 1)
            i = 0
    return stats, EXIT


# ==========================================
# Tutorial
# ==========================================
def tutorial(input_fn=input, print_fn=print):
    print_fn("🚀 五笔启动 🚀")
    print_fn("用字母代表笔画打字")
    print_fn("\033[32m横 → g\033[0m")   # green
    print_fn("\033[36m竖 → h\033[0m")   # cyan
    print_fn("\033[34m撇 → t\033[0m")   # blue
    print_fn("\033[35m捺 → y\033[0m")   # magenta
    print_fn("\033[31m折 → n\033[0m") # red

    steps = [
        ("下", "gh", "第一笔是『一』横(g)，第二部分『卜』竖(h) → gh\n请输入 [下] 的编码", ""),
        ("班", "gy", "第一部分『王』是字根, 也在(g) + 第二部分『丶』是点,在捺位(y) → gy",""),
        ("下班", "ghgy", "","下(gh) + 班(gy) → ghgy"),
        ("上", "hh", "『上』本身是字根，首笔竖(h) → hh",""),
        ("上班", "hhgy", "","上(hh) + 班(gy) → hhgy"),
        ("政策", "ghtg", "","政(gh) + 策(tg) → ghtg"),
    ]
    for word, correct, instrct, hint in steps:
        while True:
            print_fn(f"{word}: {instrct} ")
            s = input_fn(f"[{word}]: ").strip().lower()
            if s == correct:
                print_fn("✅ 对啦!")
                break
            elif s == ":exit":
                print_fn("👋 教程已退出。")
                return
            else:
                print_fn("😅 不对哦，再试一次")
                print_fn({hint})
    print_fn("\n🎉 教程完成！")


# ==========================================
# Main Entry
# ==========================================
def main() -> None:
    print("🖐️  📝 🛤️  starting ...")
                                
    level_set = build_level_set(BASE_KEYS, ADD_NEW)
    progress = read_progress(PROGRESS_FILE)
    level = int(progress.get("level", 0))
    max_level = max(level_set)

    if level == 0:
        tutorial()
        level = 1
        print(f"\033[33m🚀达到 level: {level} 解锁 {ADD_NEW.get(level, '')}\033[0m")
        known_keys = get_keys_for_level(level, level_set)
        print_wubi_table(known_world=known_keys, new_block=ADD_NEW.get(level))
        print("💡 指令提示\n")
        print("🚪 退出程序请输入 ':exit'（包含冒号）")
        print("👀 查看键位请输入 ':show'（包含冒号）\n")
    else:
        print(f"\033[94m继续 level {level}\033[0m")
        known_keys = get_keys_for_level(level, level_set)

    while True:
        print(f"\033[33m level: {level}\033[0m")
        candidate_words = select_practice_words(known_keys, COMMON_WORD_MAP, PROGRESS_FILE)
        candidate_words = candidate_words[:CANDIDATE_LIMIT_DEFAULT]

        session_stats, exit_flag = quiz_loop(candidate_words, known_keys)
        all_stats = save_progress(session_stats, PROGRESS_FILE, level=level)

        if exit_flag:
            print("👋 bye")
            break

        if wubidao_progress_policy(all_stats) and level < max_level:
            level += 1
            print(f"\033[33m🚀升级! 解锁 {ADD_NEW.get(level, '')}\033[0m")
            save_progress({}, PROGRESS_FILE, level=level)
            known_keys = get_keys_for_level(level, level_set)
            print_wubi_table(known_world=known_keys, new_block=ADD_NEW.get(level))
        elif level >= max_level:
            print(f"\033[96m🎯 已达到最高等级 {max_level}，继续巩固练习。\033[0m")
            save_progress({}, PROGRESS_FILE, level=level)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋")

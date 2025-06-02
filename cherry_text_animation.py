import turtle as t
import random
import time
import math

class CherryBlossomTextAnimation:
    def __init__(self):
        self.setup_canvas()
        self.tree_leaves = []       # 树上的文字叶子
        self.fallen_texts = []      # 掉落的文字
        self.branch_positions = []  # 记录树枝位置
        self.wind_active = False
        self.wind_strength = 0
        self.animation_running = True
        
    def setup_canvas(self):
        """设置画布"""
        self.screen = t.Screen()
        self.screen.bgcolor("#F5F5F5")  # 浅灰背景
        self.screen.setup(width=1000, height=700)
        self.screen.title("🌸 樱花飘落动画 - 按空格键切换风效果，ESC键退出")
        self.screen.tracer(0, 0)  # 关闭自动刷新
        
        # 绑定键盘事件
        self.screen.listen()
        self.screen.onkey(self.toggle_wind, "space")
        self.screen.onkey(self.reset_scene, "r")
        self.screen.onkey(self.quit_animation, "Escape")
        return self.screen

    def draw_blossom_at_tip(self, turtle_obj):
        """在枝条末端绘制花朵"""
        if random.random() < 0.7:  # 70%概率绘制花朵
            turtle_obj.color("#FFB6C1", "#FFCCCB")
            turtle_obj.begin_fill()
            for _ in range(5):  # 绘制5瓣花
                turtle_obj.circle(3, 72)
                turtle_obj.left(144)
            turtle_obj.end_fill()

    def draw_branch(self, turtle_obj, branch_len, thickness, angle, color, depth=0):
        """递归绘制树枝并记录位置"""
        if branch_len < 8:
            # 在枝条末端绘制花苞并记录位置
            self.draw_blossom_at_tip(turtle_obj)
            # 记录枝条末端位置用于放置文字，只在细枝上
            if depth > 3:  # 提高深度要求，只在更细的枝条上放文字
                pos = (turtle_obj.xcor(), turtle_obj.ycor(), depth)
                self.branch_positions.append(pos)
            return
        
        # 设置画笔属性
        turtle_obj.pensize(max(1, thickness))
        turtle_obj.color(color)
        
        # 绘制当前树枝
        turtle_obj.down()
        turtle_obj.forward(branch_len)
        
        # 在较小分支记录位置，避开主干区域
        if depth > 2 and branch_len < 30 and random.random() < 0.4:
            # 检查是否远离主干中心
            current_x = turtle_obj.xcor()
            if abs(current_x) > 20:  # 距离主干中心至少20像素
                turtle_obj.backward(branch_len // 3)
                pos = (turtle_obj.xcor(), turtle_obj.ycor(), depth)
                self.branch_positions.append(pos)
                turtle_obj.forward(branch_len // 3)
        
        # 递归绘制子树枝
        if branch_len > 15:
            # 随机分支参数
            left_angle = angle * (0.6 + random.random() * 0.8)
            right_angle = angle * (0.6 + random.random() * 0.8)
            left_len = branch_len * (0.65 + random.random() * 0.25)
            right_len = branch_len * (0.65 + random.random() * 0.25)
            
            # 左分支
            turtle_obj.left(left_angle)
            self.draw_branch(turtle_obj, left_len, thickness * 0.7, angle, color, depth + 1)
            turtle_obj.right(left_angle)
            
            # 右分支  
            turtle_obj.right(right_angle)
            self.draw_branch(turtle_obj, right_len, thickness * 0.7, angle, color, depth + 1)
            turtle_obj.left(right_angle)
        
        # 回退
        turtle_obj.up()
        turtle_obj.backward(branch_len)

    def create_text_leaves(self):
        """在树枝上创建汉字叶子，避免与树干重叠"""
        texts = [
            "吹", "绿", "草", "美", "莺", "啼", "蝶", "舞", "草", "长", "溪", "潺", "雨", "润", "露", "莹", 
            "晴", "柔", "阳", "煦", "芳", "菲", "杏", "粉", "梨", "白", "兰", "香", "樱", "飘", "萌", "芽", 
            "碧", "翠", "绯", "霞", "晖", "韶", "光", "苏", "欣", "悦", "醉", "梦", "诗", "画", "环", "佩", 
            "铃", "铛", "翩", "芊", "苒", "暄", "清", "悠", "婉", "妙", "灵", "秀", "雅", "韵", "华", "韶",  
            "鼓", "乐", "琴", "瑟", "嫣", "娆", "媚", "灿", "皎", "皎", "融", "怡", "宁", "谧", "乐", "欢", 
            "歌", "谣", "笛", "声", "曲", "调", "舞", "袖", "纱", "轻", "烟", "波", "涟", "漪", "舟", "摇", 
            "桥", "影", "亭", "台", "楼", "阁", "径", "幽", "林", "深", "泉", "鸣", "石", "润", "吻", "亲", 
            "松", "竹", "梅", "鹤", "云", "悠", "天", "蓝", "水", "秀", "山", "青", "野", "阔", "田", "园", 
            "牧", "童", "笛", "远", "村", "烟", "晨", "曦", "暮", "霭", "星", "辰", "箫", "笛", "笙", "簧",
            "月", "皎", "灯", "火", "茶", "烟", "书", "卷", "墨", "香", "笔", "韵", "纸", "鸢", "莺", "燕", 
            "蜂", "蜜", "蛙", "鸣", "蝉", "唱", "萤", "火", "鱼", "跃", "荷", "摇", "诗", "联", "谜", "语",
            "梧", "桐", "枫", "丹", "菊", "黄", "桂", "馥", "荔", "枝", "葡", "萄", "瓜", "甜", "抱", "拥", 
            "搂", "抚", "摸", "李", "酸", "杏", "熟", "桃", "饱", "梨", "脆", "樱", "甜", "莓", "鲜", "笋", 
            "嫩", "木", "匏", "音", "律", "调", "茶", "新", "酒", "醇", "糕", "香", "饼", "酥", "糖", "甜", 
            "蜜", "甘", "酥", "脆", "韵", "歌", "词", "曲", "赋", "羹", "暖", "汤", "热", "炉", "温", "被", 
            "暖", "枕", "安", "眠", "甜", "梦", "美", "明", "晨", "昏", "昼", "夜", "晓", "暮", "希", "冀", 
            "期", "待", "等", "候", "守", "护", "光", "芒", "辉", "煌", "耀", "闪", "烁", "亮", "明", "朗", 
            "照", "衣", "轻", "衫", "薄", "裙", "飘", "带", "舞", "鞋", "绣", "袜", "罗", "钗", "玉", "墨", 
            "盒", "水", "滴", "笔", "洗", "印", "泥", "色", "彩", "朱", "砂", "金", "粉", "银", "箔", "青", 
            "绿", "蓝", "靛", "紫", "橙", "黄", "赤", "白", "黑", "灰", "褐", "茶", "香", "醉", "梦", "诗", 
            "纸", "鸢", "鹞", "翔", "飞", "絮", "杨", "絮", "萍", "浮", "舟", "荡", "桨", "摇", "梅", "鹤",  
            "桥", "影", "亭", "台", "楼", "阁", "园", "林", "径", "幽", "泉", "鸣", "石", "涧", "松", "竹", 
            "晨", "曦", "朝", "暮", "晚", "昏", "星", "月", "灯", "火", "烛", "照", "明", "朗", "云", "霞", 
            "衣", "轻", "衫", "薄", "袖", "裙", "带", "钗", "佩", "铃", "铛", "鼓", "钟", "琴", "霓", "虹", 
            "棋", "书", "画", "印", "砚", "笔", "墨", "纸", "砚", "台", "架", "镇", "盒", "洗", "雾", "霭", 
            "色", "彩", "朱", "砂", "金", "粉", "银", "蓝", "靛", "紫", "橙", "黄", "白", "黑", "烟", "波", 
            "甜", "蜜", "酥", "脆", "糕", "饼", "糖", "羹", "汤", "酒", "醇", "茗", "新", "鲜", "涟", "漪", 
            "闲", "悠", "逸", "恬", "静", "安", "宁", "康", "泰", "福", "寿", "喜", "乐", "欢", "画", "歌", 
            "咏", "吟", "诵", "读", "写", "作", "赋", "词", "联", "谜", "戏", "博", "弈", "射", "谣", "笛", 
            "礼", "仪", "仁", "义", "德", "善", "美", "真", "慧", "灵", "巧", "妙", "雅", "韵", "声", "曲" ]
        
        # 过滤掉太靠近主干中心的位置
        filtered_positions = []
        for pos in self.branch_positions:
            x, y, depth = pos
            # 确保文字位置远离主干中心和地面
            if abs(x) > 30 and y > -100:  # 距离中心至少30像素，高度大于-100
                filtered_positions.append(pos)
        
        print(f"🌿 过滤后有 {len(filtered_positions)} 个合适的位置放置文字")
        
        # 使用过滤后的位置
        available_positions = filtered_positions[:len(texts)]
        
        for i, text in enumerate(texts):
            if i >= len(available_positions):
                break
                
            leaf = {
                'turtle': t.Turtle(),
                'text': text,
                'attached': True,  # 是否还在树上
                'falling': False,  # 是否正在掉落
                'fallen': False,   # 是否已经落地
            }
            
            # 设置turtle属性
            leaf['turtle'].hideturtle()
            leaf['turtle'].penup()
            leaf['turtle'].color("#FF69B4")
            leaf['turtle'].speed(0)
            
            # 使用记录的树枝位置
            branch_pos = available_positions[i]
            x, y, depth = branch_pos
            
            # 增加更大的偏移，确保远离树枝
            offset_distance = random.uniform(15, 25)  # 增大偏移距离
            offset_angle = random.uniform(0, 360)
            offset_x = offset_distance * math.cos(math.radians(offset_angle))
            offset_y = offset_distance * math.sin(math.radians(offset_angle))
            
            final_x = x + offset_x
            final_y = y + offset_y
            
            # 确保文字不会太靠近主干
            if abs(final_x) < 25:
                final_x = final_x + (25 if final_x > 0 else -25)
            
            # 位置和动画属性
            leaf['original_x'] = final_x
            leaf['original_y'] = final_y
            leaf['current_x'] = final_x
            leaf['current_y'] = final_y
            leaf['angle'] = i * 30
            leaf['swing_speed'] = random.uniform(0.02, 0.04)
            leaf['swing_range'] = random.uniform(3, 8)
            leaf['branch_depth'] = depth
            leaf['font_size'] = max(10, 14 - depth)
            
            # 掉落属性
            leaf['fall_speed_x'] = 0
            leaf['fall_speed_y'] = 0
            leaf['rotation'] = 0
            leaf['rotation_speed'] = random.uniform(-5, 5)
            
            # 绘制初始文字 - 使用带背景的方法
            font_info = ("楷体", int(leaf['font_size']), "bold")
            self.draw_text_with_background(
                leaf['turtle'], 
                text, 
                final_x, 
                final_y, 
                font_info,
                "#FF69B4",  # 文字颜色
                "#F0F8FF"   # 浅色背景
            )
            
            self.tree_leaves.append(leaf)

    def toggle_wind(self):
        """切换风效果，吹落文字"""
        self.wind_active = True
        self.wind_strength = 2.0
        print("🌬️ 春风起，叶字飘...")
        
        # 随机选择一些文字开始掉落
        attached_leaves = [leaf for leaf in self.tree_leaves if leaf['attached']]
        if attached_leaves:
            # 随机选择30-60%的叶子开始掉落
            fall_count = max(1, int(len(attached_leaves) * random.uniform(0.3, 0.8)))
            falling_leaves = random.sample(attached_leaves, fall_count)
            
            for leaf in falling_leaves:
                leaf['attached'] = False
                leaf['falling'] = True
                # 初始掉落速度
                leaf['fall_speed_x'] = random.uniform(-2, 2)
                leaf['fall_speed_y'] = random.uniform(-1, -3)

    def draw_text_with_background(self, turtle_obj, text, x, y, font_info, text_color="#FF69B4", bg_color="#FFFFFF"):
        """绘制带背景的文字，避免被遮挡"""
        # 先绘制小的背景圆圈
        turtle_obj.goto(x, y-6)  # 稍微向下偏移
        turtle_obj.color(bg_color)
        turtle_obj.begin_fill()
        turtle_obj.circle(6)  # 小背景圆圈
        turtle_obj.end_fill()
        
        # 再绘制文字
        turtle_obj.goto(x, y)
        turtle_obj.color(text_color)
        turtle_obj.write(text, align="center", font=font_info)

    def update_tree_leaves(self):
        """更新树上的文字叶子"""
        for leaf in self.tree_leaves:
            if leaf['attached']:
                # 树上的叶子轻微摆动
                leaf['angle'] += leaf['swing_speed']
                
                # 风效果
                wind_effect = self.wind_strength * random.uniform(0.5, 1.5) if self.wind_active else 0
                swing_offset = math.sin(leaf['angle']) * (leaf['swing_range'] + wind_effect * 3)
                float_offset = math.sin(leaf['angle'] * 1.2) * (1 + wind_effect * 0.5)
                
                # 更新位置
                leaf['current_x'] = leaf['original_x'] + swing_offset
                leaf['current_y'] = leaf['original_y'] + float_offset
                
                # 重绘文字（带背景）
                leaf['turtle'].clear()
                font_info = ("楷体", int(leaf['font_size']), "bold")
                self.draw_text_with_background(
                    leaf['turtle'], 
                    leaf['text'], 
                    leaf['current_x'], 
                    leaf['current_y'], 
                    font_info,
                    "#FF69B4",  # 文字颜色
                    "#F0F8FF"   # 浅色背景
                )
            
            elif leaf['falling']:
                # 掉落中的文字
                self.update_falling_text(leaf)

    def update_falling_text(self, leaf):
        """更新掉落中的文字"""
        # 物理模拟
        leaf['fall_speed_y'] -= 0.05  # 重力
        leaf['fall_speed_x'] *= 0.98  # 空气阻力
        
        # 风的影响
        if self.wind_active:
            leaf['fall_speed_x'] += random.uniform(-0.1, 0.1) * self.wind_strength
        
        # 更新位置
        leaf['current_x'] += leaf['fall_speed_x']
        leaf['current_y'] += leaf['fall_speed_y']
        
        # 旋转
        leaf['rotation'] += leaf['rotation_speed']
        
        # 检查是否落地
        if leaf['current_y'] < -200:  # 地面高度
            leaf['falling'] = False
            leaf['fallen'] = True
            # 在地面找个位置堆积
            final_x = leaf['current_x'] + random.uniform(-20, 20)
            final_y = -200 + random.uniform(-10, 5)  # 地面附近随机高度
            leaf['current_x'] = final_x
            leaf['current_y'] = final_y
            leaf['fall_speed_x'] = 0
            leaf['fall_speed_y'] = 0
            
            # 添加到地面文字堆
            self.fallen_texts.append(leaf)
            print(f"📜 '{leaf['text']}' 落地了...")
        
        # 重绘文字（掉落时也使用背景）
        leaf['turtle'].clear()
        size = max(8, leaf['font_size'] - 2)
        font_info = ("楷体", int(size), "bold")
        self.draw_text_with_background(
            leaf['turtle'], 
            leaf['text'], 
            leaf['current_x'], 
            leaf['current_y'], 
            font_info,
            "#FF1493",  # 掉落时用更鲜艳的颜色
            "#FFE4E1"   # 淡粉色背景
        )

    def update_fallen_texts(self):
        """更新地面上的文字堆积"""
        for leaf in self.fallen_texts:
            if leaf['fallen']:
                # 地面文字可能会被风稍微移动
                if self.wind_active and random.random() < 0.05:
                    leaf['current_x'] += random.uniform(-1, 1)
                
                # 确保文字在合理范围内
                leaf['current_x'] = max(-400, min(400, leaf['current_x']))
                
                # 重绘（地面文字使用简单样式）
                leaf['turtle'].clear()
                leaf['turtle'].goto(leaf['current_x'], leaf['current_y'])
                leaf['turtle'].color("#FF1493")  # 地面文字颜色
                leaf['turtle'].write(leaf['text'], align="center", 
                                   font=("楷体", 10, "normal"))

    def reset_scene(self):
        """重置场景"""
        print("🔄 重置场景...")
        
        # 清除所有文字
        for leaf in self.tree_leaves + self.fallen_texts:
            leaf['turtle'].clear()
        
        # 重置状态
        self.fallen_texts = []
        for leaf in self.tree_leaves:
            leaf['attached'] = True
            leaf['falling'] = False
            leaf['fallen'] = False
            leaf['current_x'] = leaf['original_x']
            leaf['current_y'] = leaf['original_y']
            leaf['fall_speed_x'] = 0
            leaf['fall_speed_y'] = 0
            
            # 重新绘制在树上（使用带背景的方法）
            font_info = ("楷体", int(leaf['font_size']), "bold")
            self.draw_text_with_background(
                leaf['turtle'], 
                leaf['text'], 
                leaf['current_x'], 
                leaf['current_y'], 
                font_info,
                "#FF69B4",  # 文字颜色
                "#F0F8FF"   # 浅色背景
            )
        
        self.wind_active = False
        self.wind_strength = 0

    def quit_animation(self):
        """退出动画"""
        self.animation_running = False
        print("👋 再见！感谢欣赏文字叶落...")

    def draw_tree(self):
        """绘制樱花树（优化以减少对文字的遮挡）"""
        self.branch_positions = []
        
        tree = t.Turtle()
        tree.hideturtle()
        tree.speed(0)
        tree.left(90)
        tree.up()
        tree.goto(0, -250)
        tree.down()
        
        # 绘制树干（稍微变细以减少遮挡）
        tree.color("#8B4513")
        tree.pensize(12)  # 从15减少到12
        tree.forward(80)
        
        # 绘制分支
        tree.color("#654321")
        self.draw_branch(tree, 120, 10, 30, "#654321", 0)  # 从12减少到10
        
        print(f"🌿 在 {len(self.branch_positions)} 个枝条位置准备放置文字")

    def draw_ground(self):
        """绘制地面"""
        ground = t.Turtle()
        ground.hideturtle()
        ground.speed(0)
        ground.up()
        
        # 绘制地面
        ground.goto(-500, -200)
        ground.down()
        ground.color("#90EE90")
        ground.begin_fill()
        for _ in range(2):
            ground.forward(1000)
            ground.right(90)
            ground.forward(50)
            ground.right(90)
        ground.end_fill()

    def run_animation(self):
        """运行主动画循环"""
        print("🌸 文字叶落动画启动！")
        print("按空格键触发春风，R键重置场景，ESC键退出")
        
        # 绘制顺序很重要：先背景，再树，最后文字（确保文字在最上层）
        self.draw_ground()
        self.draw_tree()        # 树在底层
        self.create_text_leaves()  # 文字在顶层
        
        print(f"🍃 在树上放置了 {len(self.tree_leaves)} 个文字叶子")
        print("💨 按空格键让春风吹落文字叶子...")
        
        # 主循环
        while self.animation_running:
            try:
                # 更新动画
                self.update_tree_leaves()
                self.update_fallen_texts()
                
                # 风力逐渐减弱
                if self.wind_active:
                    self.wind_strength *= 0.995
                    if self.wind_strength < 0.1:
                        self.wind_active = False
                        self.wind_strength = 0
                
                # 更新屏幕
                self.screen.update()
                time.sleep(0.03)
                
            except t.Terminator:
                break
            except KeyboardInterrupt:
                break
        
        # 清理
        try:
            self.screen.bye()
        except:
            pass

def main():
    """主函数"""
    try:
        animation = CherryBlossomTextAnimation()
        animation.run_animation()
    except Exception as e:
        print(f"程序遇到错误: {e}")
        print("请确保已正确安装Python和turtle库")

if __name__ == "__main__":
    main()
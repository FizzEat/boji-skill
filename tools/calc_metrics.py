#!/usr/bin/env python3
"""
calc_metrics.py - 薄拉图 / 薄肌指标速算工具
用于快速测算：
1. BMI 与薄肌身材分型象限初筛
2. BMR (基础代谢率) 与 TDEE (每日总消耗)
3. 薄肌目标热量缺口与蛋白质摄入推荐
4. 薄士学位引体向上推重比估算
"""

import sys
import argparse

def calculate_bmr(weight_kg, height_cm, age, gender="male"):
    # Mifflin-St Jeor Formula
    if gender.lower() in ["male", "m", "男"]:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

def calculate_tdee(bmr, activity_level="light"):
    multipliers = {
        "sedentary": 1.2,     # 久坐久躺，极少运动
        "light": 1.375,       # 每周 1-3 天轻度运动/通勤
        "moderate": 1.55,     # 每周 3-5 天规律力量或有氧
        "active": 1.725,      # 每天高强度训练或重体力劳动
    }
    return bmr * multipliers.get(activity_level, 1.375)

def assess_quadrant(height_cm, weight_kg, est_bodyfat=None):
    bmi = weight_kg / ((height_cm / 100) ** 2)
    
    if est_bodyfat is not None:
        bf = est_bodyfat
    else:
        # 粗略估算体脂
        bf = (1.20 * bmi) + (0.23 * 25) - 16.2  # 默认25岁男性粗估
    
    if bf < 12 and bmi < 20.5:
        category = "精瘦排骨型 (细狗，框架未开，亟需清洁增肌)"
        strategy = "热量轻度盈余 (+200-300 kcal)，主攻复合动作与背胸框架，停止过量有氧"
    elif bf >= 18 and bmi < 23.5:
        category = "泡芙人 / 隐形肥胖型 (内脏脂肪偏高，肌肉量低)"
        strategy = "身体重组 (Recomp)：维持热量平衡或微缺口 (-200 kcal)，高蛋白，主攻抗阻力量"
    elif bf >= 20 and bmi >= 23.5:
        category = "超重/脂包肌型 (代谢压力大，视觉廓形被脂肪覆盖)"
        strategy = "温和热量缺口 (-400-500 kcal)，外卖控油断精碳，早晚快走 + 极简力量课表"
    elif 11 <= bf <= 15 and bmi >= 21:
        category = "标准薄肌黄金区 (已具备穿衣显瘦脱衣有肉雏形)"
        strategy = "维持微调，打磨肩背倒三角细节，冲击薄士学位（15个引体向上）"
    else:
        category = "过渡混合型"
        strategy = "先执行4周低压外卖替换，建立规律力量习惯再行评估"
        
    return bmi, bf, category, strategy

def main():
    parser = argparse.ArgumentParser(description="薄拉图与薄肌生理指标测算工具")
    parser.add_argument("--height", type=float, required=True, help="身高 (cm)")
    parser.add_argument("--weight", type=float, required=True, help="体重 (kg)")
    parser.add_argument("--age", type=int, default=25, help="年龄 (默认 25)")
    parser.add_argument("--gender", type=str, default="male", choices=["male", "female", "男", "女"], help="性别")
    parser.add_argument("--pullups", type=int, default=0, help="目前单次最大连续引体向上数")
    parser.add_argument("--bodyfat", type=float, default=None, help="已知体脂率 (百分比)，选填")
    parser.add_argument("--activity", type=str, default="light", choices=["sedentary", "light", "moderate", "active"], help="日常活动水平")
    
    args = parser.parse_args()
    
    bmr = calculate_bmr(args.weight, args.height, args.age, args.gender)
    tdee = calculate_tdee(bmr, args.activity)
    bmi, bf, category, strategy = assess_quadrant(args.height, args.weight, args.bodyfat)
    
    protein_target = args.weight * 1.6  # 1.6g/kg
    cut_calories = tdee - 350           # 温和缺口
    
    print("=" * 55)
    print(" 🥋 薄拉图体态与代谢速测报告 (Boplato Metrics)")
    print("=" * 55)
    print(f"基础参数: 身高 {args.height:.1f}cm | 体重 {args.weight:.1f}kg | 年龄 {args.age} | BMI: {bmi:.1f}")
    print(f"体脂预估: 约 {bf:.1f}%")
    print(f"身材分型: {category}")
    print("-" * 55)
    print(f"🔥 基础代谢 (BMR): {bmr:.0f} kcal/天")
    print(f"⚡ 每日总消耗 (TDEE): {tdee:.0f} kcal/天")
    print(f"🎯 建议摄入目标: {cut_calories:.0f} kcal/天 (温和减脂/重组)")
    print(f"🥩 蛋白质底线目标: {protein_target:.0f}g / 天 (约相当于 {protein_target / 30:.1f} 个掌心高蛋白)")
    print("-" * 55)
    print(f"🏋️ 薄士学位现状 (目标: 15个连续标准引体): 当前 {args.pullups} 个")
    if args.weight < 60:
        print("   ⚠️ 注意：体重低于 60kg，薄士学位需优先增至 60kg 以上方可核验有效硬实力！")
    if args.pullups >= 15 and args.weight >= 60:
        print("   🎉 恭喜！已达成【薄士学位】考核基准，身体推重比与执行力达到硬核水准！")
    else:
        gap = max(0, 15 - args.pullups)
        print(f"   📈 距离薄士学位尚有 {gap} 个差距，建议调用 `/boji-pullup` 启动离心与高位抗阻阶梯。")
    print("-" * 55)
    print(f"💡 阶段核心指导策略:\n   {strategy}")
    print("=" * 55)

if __name__ == "__main__":
    main()

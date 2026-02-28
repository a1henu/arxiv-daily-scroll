---
layout: default
title: Automated Robotic Needle Puncture for Percutaneous Dilatational Tracheostomy
---

# Automated Robotic Needle Puncture for Percutaneous Dilatational Tracheostomy
**arXiv**：[2602.22952v1](https://arxiv.org/abs/2602.22952) · [PDF](https://arxiv.org/pdf/2602.22952.pdf)  
**作者**：Yuan Tang, Bruno V. Adorno, Brendan A. McGrath, Andrew Weightman  

**一句话要点**：提出自动化机器人针穿刺系统以提高经皮扩张气管切开术的准确性和安全性

**关键词**：机器人辅助手术, 经皮扩张气管切开术, 自适应控制, 电磁导航, 针穿刺自动化, 手术精度提升

## 3 点简述
- 经皮扩张气管切开术的针穿刺步骤存在位置和角度误差，可能导致严重并发症
- 系统使用速度控制机器人，基于电磁传感器位姿数据，采用自适应约束控制器在线调整参数并避免碰撞
- 在模拟和人体模型实验中，位置误差中位数为1.7毫米，角度偏差为4.13度，验证了系统的可行性

## 摘要（原文）

> Percutaneous dilatational tracheostomy (PDT) is frequently performed on patients in intensive care units for prolonged mechanical ventilation. The needle puncture, as the most critical step of PDT, could lead to adverse consequences such as major bleeding and posterior tracheal wall perforation if performed inaccurately. Current practices of PDT puncture are all performed manually with no navigation assistance, which leads to large position and angular errors (5 mm and 30 degree). To improve the accuracy and reduce the difficulty of the PDT procedure, we propose a system that automates the needle insertion using a velocity-controlled robotic manipulator. Guided using pose data from two electromagnetic sensors, one at the needle tip and the other inside the trachea, the robotic system uses an adaptive constrained controller to adapt the uncertain kinematic parameters online and avoid collisions with the patient's body and tissues near the target. Simulations were performed to validate the controller's implementation, and then four hundred PDT punctures were performed on a mannequin to evaluate the position and angular accuracy. The absolute median puncture position error was 1.7 mm (IQR: 1.9 mm) and midline deviation was 4.13 degree (IQR: 4.55 degree), measured by the sensor inside the trachea. The small deviations from the nominal puncture in a simulated experimental setup and formal guarantees of collision-free insertions suggest the feasibility of the robotic PDT puncture.


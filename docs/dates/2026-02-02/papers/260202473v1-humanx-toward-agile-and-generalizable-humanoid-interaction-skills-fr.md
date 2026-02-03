---
layout: default
title: HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos
---

# HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos
**arXiv**：[2602.02473v1](https://arxiv.org/abs/2602.02473) · [PDF](https://arxiv.org/pdf/2602.02473.pdf)  
**作者**：Yinhuai Wang, Qihan Zhao, Yuen Fui Lau, Runyi Yu, Hok Wai Tsui, Qifeng Chen, Jingbo Wang, Jiangmiao Pang, Ping Tan  

**一句话要点**：提出HumanX框架，从人类视频学习通用人形机器人交互技能，无需任务特定奖励。

**关键词**：人形机器人, 交互技能学习, 视频模仿学习, 数据生成, 零样本迁移, 通用技能框架

## 3 点简述
- 核心问题：人形机器人交互技能学习受限于数据稀缺和任务特定奖励工程，难以扩展。
- 方法要点：集成XGen数据生成和XMimic模仿学习，从视频合成物理合理数据并学习通用技能。
- 实验或效果：在五个领域学习10种技能，零样本迁移到物理机器人，泛化成功率比先前方法高8倍以上。

## 摘要（原文）

> Enabling humanoid robots to perform agile and adaptive interactive tasks has long been a core challenge in robotics. Current approaches are bottlenecked by either the scarcity of realistic interaction data or the need for meticulous, task-specific reward engineering, which limits their scalability. To narrow this gap, we present HumanX, a full-stack framework that compiles human video into generalizable, real-world interaction skills for humanoids, without task-specific rewards. HumanX integrates two co-designed components: XGen, a data generation pipeline that synthesizes diverse and physically plausible robot interaction data from video while supporting scalable data augmentation; and XMimic, a unified imitation learning framework that learns generalizable interaction skills. Evaluated across five distinct domains--basketball, football, badminton, cargo pickup, and reactive fighting--HumanX successfully acquires 10 different skills and transfers them zero-shot to a physical Unitree G1 humanoid. The learned capabilities include complex maneuvers such as pump-fake turnaround fadeaway jumpshots without any external perception, as well as interactive tasks like sustained human-robot passing sequences over 10 consecutive cycles--learned from a single video demonstration. Our experiments show that HumanX achieves over 8 times higher generalization success than prior methods, demonstrating a scalable and task-agnostic pathway for learning versatile, real-world robot interactive skills.


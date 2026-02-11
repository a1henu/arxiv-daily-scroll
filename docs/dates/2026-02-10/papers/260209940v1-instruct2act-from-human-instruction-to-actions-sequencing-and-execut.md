---
layout: default
title: Instruct2Act: From Human Instruction to Actions Sequencing and Execution via Robot Action Network for Robotic Manipulation
---

# Instruct2Act: From Human Instruction to Actions Sequencing and Execution via Robot Action Network for Robotic Manipulation
**arXiv**：[2602.09940v1](https://arxiv.org/abs/2602.09940) · [PDF](https://arxiv.org/pdf/2602.09940.pdf)  
**作者**：Archit Sharma, Dharmendra Sharma, John Rebeiro, Peeyush Thakur, Narendra Dhar, Laxmidhar Behera  

**一句话要点**：提出Instruct2Act和RAN以解决资源受限下机器人从自然语言指令到精确动作序列的实时执行问题

**关键词**：机器人操作, 自然语言指令, 动作序列解析, 轨迹生成, 视觉引导, 轻量级系统

## 3 点简述
- 核心问题：机器人在资源受限环境中难以可靠执行自由形式的人类指令
- 方法要点：使用Instruct2Act解析指令为动作序列，RAN结合DATRN和YOLOv8生成控制轨迹
- 实验或效果：在自定义数据集上达到91.5%子动作预测准确率，真实机器人任务成功率90%

## 摘要（原文）

> Robots often struggle to follow free-form human instructions in real-world settings due to computational and sensing limitations. We address this gap with a lightweight, fully on-device pipeline that converts natural-language commands into reliable manipulation. Our approach has two stages: (i) the instruction to actions module (Instruct2Act), a compact BiLSTM with a multi-head-attention autoencoder that parses an instruction into an ordered sequence of atomic actions (e.g., reach, grasp, move, place); and (ii) the robot action network (RAN), which uses the dynamic adaptive trajectory radial network (DATRN) together with a vision-based environment analyzer (YOLOv8) to generate precise control trajectories for each sub-action. The entire system runs on a modest system with no cloud services. On our custom proprietary dataset, Instruct2Act attains 91.5% sub-actions prediction accuracy while retaining a small footprint. Real-robot evaluations across four tasks (pick-place, pick-pour, wipe, and pick-give) yield an overall 90% success; sub-action inference completes in < 3.8s, with end-to-end executions in 30-60s depending on task complexity. These results demonstrate that fine-grained instruction-to-action parsing, coupled with DATRN-based trajectory generation and vision-guided grounding, provides a practical path to deterministic, real-time manipulation in resource-constrained, single-camera settings.


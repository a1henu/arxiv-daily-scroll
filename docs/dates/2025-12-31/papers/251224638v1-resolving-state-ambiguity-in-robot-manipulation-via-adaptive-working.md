---
layout: default
title: Resolving State Ambiguity in Robot Manipulation via Adaptive Working Memory Recoding
---

# Resolving State Ambiguity in Robot Manipulation via Adaptive Working Memory Recoding
**arXiv**：[2512.24638v1](https://arxiv.org/abs/2512.24638) · [PDF](https://arxiv.org/pdf/2512.24638.pdf)  
**作者**：Qingda Hu, Ziheng Qiu, Zijun Xu, Kaizhao Zhang, Xizhou Bu, Zuolei Sun, Bo Zhang, Jieru Zhao, Zhongxue Gan, Wenchao Ding  

**一句话要点**：提出自适应工作记忆重编码策略PAM以解决机器人操作中的状态歧义问题

**关键词**：状态歧义, 自适应工作记忆, 长历史窗口, 分层特征提取, 上下文路由器, 机器人操作

## 3 点简述
- 核心问题：机器人操作中相同观测对应多行为轨迹，需从历史中提取正确信息识别任务阶段
- 方法要点：采用分层特征提取器、上下文路由器和辅助重构目标，支持长历史窗口且推理速度快
- 实验或效果：在7个任务中验证PAM能同时处理多状态歧义场景，保持20Hz以上推理速度

## 摘要（原文）

> State ambiguity is common in robotic manipulation. Identical observations may correspond to multiple valid behavior trajectories. The visuomotor policy must correctly extract the appropriate types and levels of information from the history to identify the current task phase. However, naively extending the history window is computationally expensive and may cause severe overfitting. Inspired by the continuous nature of human reasoning and the recoding of working memory, we introduce PAM, a novel visuomotor Policy equipped with Adaptive working Memory. With minimal additional training cost in a two-stage manner, PAM supports a 300-frame history window while maintaining high inference speed. Specifically, a hierarchical frame feature extractor yields two distinct representations for motion primitives and temporal disambiguation. For compact representation, a context router with range-specific queries is employed to produce compact context features across multiple history lengths. And an auxiliary objective of reconstructing historical information is introduced to ensure that the context router acts as an effective bottleneck. We meticulously design 7 tasks and verify that PAM can handle multiple scenarios of state ambiguity simultaneously. With a history window of approximately 10 seconds, PAM still supports stable training and maintains inference speeds above 20Hz. Project website: https://tinda24.github.io/pam/


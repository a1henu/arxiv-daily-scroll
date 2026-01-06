---
layout: default
title: CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding
---

# CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding
**arXiv**：[2601.02295v1](https://arxiv.org/abs/2601.02295) · [PDF](https://arxiv.org/pdf/2601.02295.pdf)  
**作者**：Chenyang Ma, Guangyu Yang, Kai Lu, Shitong Xu, Bill Byrne, Niki Trigoni, Andrew Markham  

**一句话要点**：提出CycleVLA系统，通过子任务回溯和最小贝叶斯风险解码实现视觉-语言-动作模型的主动自校正。

**关键词**：视觉-语言-动作模型, 主动自校正, 子任务回溯, 最小贝叶斯风险解码, 机器人失败预测, 测试时缩放

## 3 点简述
- 当前机器人失败检测与校正多为事后处理，仅在失败发生后分析错误并应用校正。
- CycleVLA集成进度感知VLA、基于VLM的失败预测器和规划器，以及基于MBR的解码策略，实现执行中的主动失败预测与恢复。
- 实验表明CycleVLA提升训练良好和不足的VLA性能，MBR作为零样本测试时缩放策略有效。

## 摘要（原文）

> Current work on robot failure detection and correction typically operate in a post hoc manner, analyzing errors and applying corrections only after failures occur. This work introduces CycleVLA, a system that equips Vision-Language-Action models (VLAs) with proactive self-correction, the capability to anticipate incipient failures and recover before they fully manifest during execution. CycleVLA achieves this by integrating a progress-aware VLA that flags critical subtask transition points where failures most frequently occur, a VLM-based failure predictor and planner that triggers subtask backtracking upon predicted failure, and a test-time scaling strategy based on Minimum Bayes Risk (MBR) decoding to improve retry success after backtracking. Extensive experiments show that CycleVLA improves performance for both well-trained and under-trained VLAs, and that MBR serves as an effective zero-shot test-time scaling strategy for VLAs. Project Page: https://dannymcy.github.io/cyclevla/


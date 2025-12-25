---
layout: default
title: RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic
---

# RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic
**arXiv**：[2512.21220v1](https://arxiv.org/abs/2512.21220) · [PDF](https://arxiv.org/pdf/2512.21220.pdf)  
**作者**：Le Wang, Zonghao Ying, Xiao Yang, Quanchen Zou, Zhenfei Yin, Tianlin Li, Jian Yang, Yaodong Yang, Aishan Liu, Xianglong Liu  

**一句话要点**：提出RoboSafe，通过可执行安全逻辑保护具身智能体免受危险指令影响。

**关键词**：具身智能体安全, 运行时安全护栏, 可执行安全逻辑, 混合推理, 多模态观察, 物理机器人评估

## 3 点简述
- 具身智能体易受动态环境中隐含风险威胁，现有防御方法难以有效应对。
- RoboSafe结合后向反思与前向预测推理，基于混合长短安全记忆生成可执行安全谓词。
- 实验显示RoboSafe显著减少危险动作，保持任务性能，并在真实机器人上验证实用性。

## 摘要（原文）

> Embodied agents powered by vision-language models (VLMs) are increasingly capable of executing complex real-world tasks, yet they remain vulnerable to hazardous instructions that may trigger unsafe behaviors. Runtime safety guardrails, which intercept hazardous actions during task execution, offer a promising solution due to their flexibility. However, existing defenses often rely on static rule filters or prompt-level control, which struggle to address implicit risks arising in dynamic, temporally dependent, and context-rich environments. To address this, we propose RoboSafe, a hybrid reasoning runtime safeguard for embodied agents through executable predicate-based safety logic. RoboSafe integrates two complementary reasoning processes on a Hybrid Long-Short Safety Memory. We first propose a Backward Reflective Reasoning module that continuously revisits recent trajectories in short-term memory to infer temporal safety predicates and proactively triggers replanning when violations are detected. We then propose a Forward Predictive Reasoning module that anticipates upcoming risks by generating context-aware safety predicates from the long-term safety memory and the agent's multimodal observations. Together, these components form an adaptive, verifiable safety logic that is both interpretable and executable as code. Extensive experiments across multiple agents demonstrate that RoboSafe substantially reduces hazardous actions (-36.8% risk occurrence) compared with leading baselines, while maintaining near-original task performance. Real-world evaluations on physical robotic arms further confirm its practicality. Code will be released upon acceptance.


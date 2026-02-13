---
layout: default
title: DeepSight: An All-in-One LM Safety Toolkit
---

# DeepSight: An All-in-One LM Safety Toolkit
**arXiv**：[2602.12092v1](https://arxiv.org/abs/2602.12092) · [PDF](https://arxiv.org/pdf/2602.12092.pdf)  
**作者**：Bo Zhang, Jiaxuan Guo, Lijun Li, Dongrui Liu, Sujin Chen, Guanxu Chen, Zhijie Zheng, Qihao Lin, Lewen Yan, Chen Qian, Yijin Zhou, Yuyao Wu, Shaoxiong Guo, Tianyi Du, Jingyi Yang, Xuhao Hu, Ziqi Miao, Xiaoya Lu, Jing Shao, Xia Hu  

**一句话要点**：提出DeepSight开源工具包，集成大模型安全评估与诊断以解决现有工具分离问题。

**关键词**：大模型安全, 安全评估, 安全诊断, 开源工具包, 白盒分析

## 3 点简述
- 核心问题：现有大模型安全工具分离，评估仅定位外部风险，诊断缺乏具体场景关联。
- 方法要点：通过统一任务和数据协议，连接评估与诊断阶段，实现从黑盒到白盒的洞察。
- 实验或效果：DeepSight是首个支持前沿AI风险评估及联合安全评估与诊断的开源工具包。

## 摘要（原文）

> As the development of Large Models (LMs) progresses rapidly, their safety is also a priority. In current Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) safety workflow, evaluation, diagnosis, and alignment are often handled by separate tools. Specifically, safety evaluation can only locate external behavioral risks but cannot figure out internal root causes. Meanwhile, safety diagnosis often drifts from concrete risk scenarios and remains at the explainable level. In this way, safety alignment lack dedicated explanations of changes in internal mechanisms, potentially degrading general capabilities. To systematically address these issues, we propose an open-source project, namely DeepSight, to practice a new safety evaluation-diagnosis integrated paradigm. DeepSight is low-cost, reproducible, efficient, and highly scalable large-scale model safety evaluation project consisting of a evaluation toolkit DeepSafe and a diagnosis toolkit DeepScan. By unifying task and data protocols, we build a connection between the two stages and transform safety evaluation from black-box to white-box insight. Besides, DeepSight is the first open source toolkit that support the frontier AI risk evaluation and joint safety evaluation and diagnosis.


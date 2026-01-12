---
layout: default
title: Can We Predict Before Executing Machine Learning Agents?
---

# Can We Predict Before Executing Machine Learning Agents?
**arXiv**：[2601.05930v1](https://arxiv.org/abs/2601.05930) · [PDF](https://arxiv.org/pdf/2601.05930.pdf)  
**作者**：Jingsheng Zheng, Jintian Zhang, Yujie Luo, Yuren Mao, Yunjun Gao, Lun Du, Huajun Chen, Ningyu Zhang  

**一句话要点**：提出FOREAGENT框架以解决自主机器学习代理的执行瓶颈问题

**关键词**：自主机器学习代理, 执行瓶颈, 预测推理, 世界模型, 数据为中心解决方案偏好, 预测-验证循环

## 3 点简述
- 核心问题：自主机器学习代理依赖昂贵的物理执行导致执行瓶颈
- 方法要点：通过内部化执行先验，用预测推理替代运行时检查，采用Predict-then-Verify循环
- 实验或效果：在18,438对比较数据上，LLMs预测准确率达61.5%，FOREAGENT加速收敛6倍，性能提升6%

## 摘要（原文）

> Autonomous machine learning agents have revolutionized scientific discovery, yet they remain constrained by a Generate-Execute-Feedback paradigm. Previous approaches suffer from a severe Execution Bottleneck, as hypothesis evaluation relies strictly on expensive physical execution. To bypass these physical constraints, we internalize execution priors to substitute costly runtime checks with instantaneous predictive reasoning, drawing inspiration from World Models. In this work, we formalize the task of Data-centric Solution Preference and construct a comprehensive corpus of 18,438 pairwise comparisons. We demonstrate that LLMs exhibit significant predictive capabilities when primed with a Verified Data Analysis Report, achieving 61.5% accuracy and robust confidence calibration. Finally, we instantiate this framework in FOREAGENT, an agent that employs a Predict-then-Verify loop, achieving a 6x acceleration in convergence while surpassing execution-based baselines by +6%. Our code and dataset will be publicly available soon at https://github.com/zjunlp/predict-before-execute.


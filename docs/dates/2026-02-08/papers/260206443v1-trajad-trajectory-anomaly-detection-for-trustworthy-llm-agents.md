---
layout: default
title: TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents
---

# TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents
**arXiv**：[2602.06443v1](https://arxiv.org/abs/2602.06443) · [PDF](https://arxiv.org/pdf/2602.06443.pdf)  
**作者**：Yibing Liu, Chong Zhang, Zhongyi Han, Hansong Liu, Yong Wang, Yang Yu, Xiaoyan Wang, Yilong Yin  

**一句话要点**：提出TrajAD轨迹异常检测方法，以增强LLM代理的运行时可信度

**关键词**：轨迹异常检测, LLM代理可信度, 过程监督, 细粒度验证, 运行时监控

## 3 点简述
- 核心问题：现有LLM代理安全措施聚焦静态输入输出，缺乏对中间执行过程的异常检测与定位
- 方法要点：构建TrajBench数据集，训练TrajAD专用验证器，实现细粒度过程监督
- 实验或效果：TrajAD在基准测试中优于基线，证明专用监督对提升代理可靠性至关重要

## 摘要（原文）

> We address the problem of runtime trajectory anomaly detection, a critical capability for enabling trustworthy LLM agents. Current safety measures predominantly focus on static input/output filtering. However, we argue that ensuring LLM agents reliability requires auditing the intermediate execution process. In this work, we formulate the task of Trajectory Anomaly Detection. The goal is not merely detection, but precise error localization. This capability is essential for enabling efficient rollback-and-retry. To achieve this, we construct TrajBench, a dataset synthesized via a perturb-and-complete strategy to cover diverse procedural anomalies. Using this benchmark, we investigate the capability of models in process supervision. We observe that general-purpose LLMs, even with zero-shot prompting, struggle to identify and localize these anomalies. This reveals that generalized capabilities do not automatically translate to process reliability. To address this, we propose TrajAD, a specialized verifier trained with fine-grained process supervision. Our approach outperforms baselines, demonstrating that specialized supervision is essential for building trustworthy agents.


---
layout: default
title: GSR: Learning Structured Reasoning for Embodied Manipulation
---

# GSR: Learning Structured Reasoning for Embodied Manipulation
**arXiv**：[2602.01693v1](https://arxiv.org/abs/2602.01693) · [PDF](https://arxiv.org/pdf/2602.01693.pdf)  
**作者**：Kewei Hu, Michael Zhang, Wei Ying, Tianhao Liu, Guoqiang Hao, Zimeng Li, Wanchan Yu, Jiajian Jing, Fangwen Chen, Hanwen Kang  

**一句话要点**：提出基于场景图的结构化推理方法GSR，以解决具身智能体在长时程操作中的空间一致性和因果依赖问题

**关键词**：具身操作, 结构化推理, 场景图, 长时程任务, 零样本泛化

## 3 点简述
- 现有方法将任务推理隐式嵌入高维表征，难以分离任务结构与感知变化
- GSR通过语义场景图显式建模世界状态演化，在物理空间中进行逐步推理
- 构建大规模数据集Manip-Cognition-1.6M，在多个基准测试中显著提升零样本泛化能力

## 摘要（原文）

> Despite rapid progress, embodied agents still struggle with long-horizon manipulation that requires maintaining spatial consistency, causal dependencies, and goal constraints. A key limitation of existing approaches is that task reasoning is implicitly embedded in high-dimensional latent representations, making it challenging to separate task structure from perceptual variability. We introduce Grounded Scene-graph Reasoning (GSR), a structured reasoning paradigm that explicitly models world-state evolution as transitions over semantically grounded scene graphs. By reasoning step-wise over object states and spatial relations, rather than directly mapping perception to actions, GSR enables explicit reasoning about action preconditions, consequences, and goal satisfaction in a physically grounded space. To support learning such reasoning, we construct Manip-Cognition-1.6M, a large-scale dataset that jointly supervises world understanding, action planning, and goal interpretation. Extensive evaluations across RLBench, LIBERO, GSR-benchmark, and real-world robotic tasks show that GSR significantly improves zero-shot generalization and long-horizon task completion over prompting-based baselines. These results highlight explicit world-state representations as a key inductive bias for scalable embodied reasoning.


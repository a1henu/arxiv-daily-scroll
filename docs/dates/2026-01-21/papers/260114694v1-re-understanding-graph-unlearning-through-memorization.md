---
layout: default
title: Re-understanding Graph Unlearning through Memorization
---

# Re-understanding Graph Unlearning through Memorization
**arXiv**：[2601.14694v1](https://arxiv.org/abs/2601.14694) · [PDF](https://arxiv.org/pdf/2601.14694.pdf)  
**作者**：Pengfei Ding, Yan Wang, Guanfeng Liu  

**一句话要点**：提出基于记忆化的图遗忘框架MGU，以解决图神经网络中遗忘任务评估不准确和效果差的问题。

**关键词**：图神经网络, 图遗忘, 记忆化, 自适应策略, 评估协议, Web应用

## 3 点简述
- 核心问题：现有图遗忘方法缺乏对遗忘效果关键因素的理解，导致评估不准确、任务处理无效和协议不匹配。
- 方法要点：从记忆化角度理解图遗忘，MGU提供准确难度评估、自适应遗忘策略和全面评估协议。
- 实验或效果：在十个真实图数据上，MGU在遗忘质量、计算效率和效用保持方面优于现有基线。

## 摘要（原文）

> Graph unlearning (GU), which removes nodes, edges, or features from trained graph neural networks (GNNs), is crucial in Web applications where graph data may contain sensitive, mislabeled, or malicious information. However, existing GU methods lack a clear understanding of the key factors that determine unlearning effectiveness, leading to three fundamental limitations: (1) impractical and inaccurate GU difficulty assessment due to test-access requirements and invalid assumptions, (2) ineffectiveness on hard-to-unlearn tasks, and (3) misaligned evaluation protocols that overemphasize easy tasks and fail to capture true forgetting capability. To address these issues, we establish GNN memorization as a new perspective for understanding graph unlearning and propose MGU, a Memorization-guided Graph Unlearning framework. MGU achieves three key advances: it provides accurate and practical difficulty assessment across different GU tasks, develops an adaptive strategy that dynamically adjusts unlearning objectives based on difficulty levels, and establishes a comprehensive evaluation protocol that aligns with practical requirements. Extensive experiments on ten real-world graphs demonstrate that MGU consistently outperforms state-of-the-art baselines in forgetting quality, computational efficiency, and utility preservation.


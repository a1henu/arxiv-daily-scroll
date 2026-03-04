---
layout: default
title: ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments
---

# ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments
**arXiv**：[2603.03198v1](https://arxiv.org/abs/2603.03198) · [PDF](https://arxiv.org/pdf/2603.03198.pdf)  
**作者**：Ziyang Gong, Zehang Luo, Anke Tang, Zhe Liu, Shi Fu, Zhi Hou, Ganlin Yang, Weiyun Wang, Xiaofeng Wang, Jianbo Liu, Gen Luo, Haolan Kang, Shuang Luo, Yue Zhou, Yong Luo, Li Shen, Xiaosong Jia, Yao Mu, Xue Yang, Chunxiao Liu, Junchi Yan, Hengshuang Zhao, Dacheng Tao, Xiaogang Wang  

**一句话要点**：提出ACE-Brain-0通用基础大脑，以空间智能为共享支架统一多模态大语言模型，解决异构具身智能的泛化难题。

**关键词**：空间智能, 异构具身智能, 多模态大语言模型, 模型合并, 通用基础大脑, 泛化能力

## 3 点简述
- 核心问题：异构具身智能（如自动驾驶、机器人）在统一模型训练中面临长尾数据、梯度干扰和灾难性遗忘，难以平衡通用泛化与领域专精。
- 方法要点：采用Scaffold-Specialize-Reconcile范式，先建立共享空间智能基础，再培养领域专家，最后通过无数据模型合并协调，并应用Group Relative Policy Optimization增强能力。
- 实验或效果：在24个空间和具身相关基准测试中，ACE-Brain-0实现了竞争性甚至最先进的性能。

## 摘要（原文）

> Universal embodied intelligence demands robust generalization across heterogeneous embodiments, such as autonomous driving, robotics, and unmanned aerial vehicles (UAVs). However, existing embodied brain in training a unified model over diverse embodiments frequently triggers long-tail data, gradient interference, and catastrophic forgetting, making it notoriously difficult to balance universal generalization with domain-specific proficiency. In this report, we introduce ACE-Brain-0, a generalist foundation brain that unifies spatial reasoning, autonomous driving, and embodied manipulation within a single multimodal large language model~(MLLM). Our key insight is that spatial intelligence serves as a universal scaffold across diverse physical embodiments: although vehicles, robots, and UAVs differ drastically in morphology, they share a common need for modeling 3D mental space, making spatial cognition a natural, domain-agnostic foundation for cross-embodiment transfer. Building on this insight, we propose the Scaffold-Specialize-Reconcile~(SSR) paradigm, which first establishes a shared spatial foundation, then cultivates domain-specialized experts, and finally harmonizes them through data-free model merging. Furthermore, we adopt Group Relative Policy Optimization~(GRPO) to strengthen the model's comprehensive capability. Extensive experiments demonstrate that ACE-Brain-0 achieves competitive and even state-of-the-art performance across 24 spatial and embodiment-related benchmarks.


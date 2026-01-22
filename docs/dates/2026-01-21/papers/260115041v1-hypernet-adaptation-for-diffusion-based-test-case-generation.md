---
layout: default
title: HyperNet-Adaptation for Diffusion-Based Test Case Generation
---

# HyperNet-Adaptation for Diffusion-Based Test Case Generation
**arXiv**：[2601.15041v1](https://arxiv.org/abs/2601.15041) · [PDF](https://arxiv.org/pdf/2601.15041.pdf)  
**作者**：Oliver Weißl, Vincenzo Riccio, Severin Kacianka, Andrea Stocco  

**一句话要点**：提出HyNeA方法，通过超网络实现扩散模型的高效可控生成，以解决深度学习系统可靠性测试中生成真实失败案例的挑战。

**关键词**：扩散模型, 测试生成, 超网络, 可控生成, 深度学习测试, 实例级调优

## 3 点简述
- 核心问题：传统对抗攻击和生成测试方法在真实失败案例生成上存在局限性，如计算成本高或可控性差。
- 方法要点：利用超网络提供数据集无关的可控性，支持实例级调优，无需依赖特定架构或失败标签数据。
- 实验或效果：相比现有方法，HyNeA提高了可控性和测试多样性，并在无失败标签领域展现出泛化能力。

## 摘要（原文）

> The increasing deployment of deep learning systems requires systematic evaluation of their reliability in real-world scenarios. Traditional gradient-based adversarial attacks introduce small perturbations that rarely correspond to realistic failures and mainly assess robustness rather than functional behavior. Generative test generation methods offer an alternative but are often limited to simple datasets or constrained input domains. Although diffusion models enable high-fidelity image synthesis, their computational cost and limited controllability restrict their applicability to large-scale testing. We present HyNeA, a generative testing method that enables direct and efficient control over diffusion-based generation. HyNeA provides dataset-free controllability through hypernetworks, allowing targeted manipulation of the generative process without relying on architecture-specific conditioning mechanisms or dataset-driven adaptations such as fine-tuning. HyNeA employs a distinct training strategy that supports instance-level tuning to identify failure-inducing test cases without requiring datasets that explicitly contain examples of similar failures. This approach enables the targeted generation of realistic failure cases at substantially lower computational cost than search-based methods. Experimental results show that HyNeA improves controllability and test diversity compared to existing generative test generators and generalizes to domains where failure-labeled training data is unavailable.


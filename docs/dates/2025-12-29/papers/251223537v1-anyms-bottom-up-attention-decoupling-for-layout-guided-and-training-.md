---
layout: default
title: AnyMS: Bottom-up Attention Decoupling for Layout-guided and Training-free Multi-subject Customization
---

# AnyMS: Bottom-up Attention Decoupling for Layout-guided and Training-free Multi-subject Customization
**arXiv**：[2512.23537v1](https://arxiv.org/abs/2512.23537) · [PDF](https://arxiv.org/pdf/2512.23537.pdf)  
**作者**：Binhe Yu, Zhen Wang, Kexin Li, Yuqian Yuan, Wenqiao Zhang, Long Chen, Juncheng Li, Jun Xiao, Yueting Zhuang  

**一句话要点**：提出AnyMS框架，通过自下而上注意力解耦实现无训练、布局引导的多主体定制生成

**关键词**：多主体定制, 布局引导生成, 注意力解耦, 无训练框架, 扩散模型, 图像合成

## 3 点简述
- 核心问题：现有方法难以平衡文本对齐、主体身份保持和布局控制，且依赖额外训练限制可扩展性
- 方法要点：引入全局和局部双级注意力解耦机制，结合预训练图像适配器，无需训练即可整合文本、主体图像和布局约束
- 实验或效果：实验表明AnyMS达到先进性能，支持复杂组合并扩展到更多主体

## 摘要（原文）

> Multi-subject customization aims to synthesize multiple user-specified subjects into a coherent image. To address issues such as subjects missing or conflicts, recent works incorporate layout guidance to provide explicit spatial constraints. However, existing methods still struggle to balance three critical objectives: text alignment, subject identity preservation, and layout control, while the reliance on additional training further limits their scalability and efficiency. In this paper, we present AnyMS, a novel training-free framework for layout-guided multi-subject customization. AnyMS leverages three input conditions: text prompt, subject images, and layout constraints, and introduces a bottom-up dual-level attention decoupling mechanism to harmonize their integration during generation. Specifically, global decoupling separates cross-attention between textual and visual conditions to ensure text alignment. Local decoupling confines each subject's attention to its designated area, which prevents subject conflicts and thus guarantees identity preservation and layout control. Moreover, AnyMS employs pre-trained image adapters to extract subject-specific features aligned with the diffusion model, removing the need for subject learning or adapter tuning. Extensive experiments demonstrate that AnyMS achieves state-of-the-art performance, supporting complex compositions and scaling to a larger number of subjects.


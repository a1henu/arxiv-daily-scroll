---
layout: default
title: Neural Clothing Tryer: Customized Virtual Try-On via Semantic Enhancement and Controlling Diffusion Model
---

# Neural Clothing Tryer: Customized Virtual Try-On via Semantic Enhancement and Controlling Diffusion Model
**arXiv**：[2601.22838v1](https://arxiv.org/abs/2601.22838) · [PDF](https://arxiv.org/pdf/2601.22838.pdf)  
**作者**：Zhijing Yang, Weiwei Zhang, Mingliang Yang, Siyuan Peng, Yukai Shi, Junpeng Tan, Tianshui Chen, Liruo Zhong  

**一句话要点**：提出Neural Clothing Tryer框架，通过语义增强与控制扩散模型实现定制化虚拟试穿

**关键词**：定制化虚拟试穿, 扩散模型, 语义增强, 语义控制, 虚拟试穿, 多模态学习

## 3 点简述
- 核心问题：解决定制化虚拟试穿任务，需在保持服装细节的同时编辑模特外观、姿态和属性。
- 方法要点：引入语义增强模块和语义控制模块，利用扩散模型提升服装语义保留和灵活编辑能力。
- 实验或效果：在公开基准测试中表现优异，验证了框架的有效性和灵活性。

## 摘要（原文）

> This work aims to address a novel Customized Virtual Try-ON (Cu-VTON) task, enabling the superimposition of a specified garment onto a model that can be customized in terms of appearance, posture, and additional attributes. Compared with traditional VTON task, it enables users to tailor digital avatars to their individual preferences, thereby enhancing the virtual fitting experience with greater flexibility and engagement. To address this task, we introduce a Neural Clothing Tryer (NCT) framework, which exploits the advanced diffusion models equipped with semantic enhancement and controlling modules to better preserve semantic characterization and textural details of the garment and meanwhile facilitating the flexible editing of the model's postures and appearances. Specifically, NCT introduces a semantic-enhanced module to take semantic descriptions of garments and utilizes a visual-language encoder to learn aligned features across modalities. The aligned features are served as condition input to the diffusion model to enhance the preservation of the garment's semantics. Then, a semantic controlling module is designed to take the garment image, tailored posture image, and semantic description as input to maintain garment details while simultaneously editing model postures, expressions, and various attributes. Extensive experiments on the open available benchmark demonstrate the superior performance of the proposed NCT framework.


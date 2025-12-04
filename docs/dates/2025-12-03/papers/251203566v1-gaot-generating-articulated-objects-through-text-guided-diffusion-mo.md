---
layout: default
title: GAOT: Generating Articulated Objects Through Text-Guided Diffusion Models
---

# GAOT: Generating Articulated Objects Through Text-Guided Diffusion Models
**arXiv**：[2512.03566v1](https://arxiv.org/abs/2512.03566) · [PDF](https://arxiv.org/pdf/2512.03566.pdf)  
**作者**：Hao Sun, Lei Fan, Donglin Di, Shaohui Liu  

**一句话要点**：提出GAOT框架，通过文本引导扩散模型生成铰接物体，解决文本描述与3D表示间的差距。

**关键词**：铰接物体生成, 文本引导生成, 扩散模型, 超图学习, 3D表示学习

## 3 点简述
- 核心问题：现有铰接物体生成模型难以基于文本提示进行条件生成，文本与3D表示间存在显著差距。
- 方法要点：采用三阶段框架，包括点云生成、超图学习细化和扩散模型生成关节，利用图结构表示物体部件。
- 实验或效果：在PartNet-Mobility数据集上验证，通过定性和定量实验展示优于先前方法的性能。

## 摘要（原文）

> Articulated object generation has seen increasing advancements, yet existing models often lack the ability to be conditioned on text prompts. To address the significant gap between textual descriptions and 3D articulated object representations, we propose GAOT, a three-phase framework that generates articulated objects from text prompts, leveraging diffusion models and hypergraph learning in a three-step process. First, we fine-tune a point cloud generation model to produce a coarse representation of objects from text prompts. Given the inherent connection between articulated objects and graph structures, we design a hypergraph-based learning method to refine these coarse representations, representing object parts as graph vertices. Finally, leveraging a diffusion model, the joints of articulated objects-represented as graph edges-are generated based on the object parts. Extensive qualitative and quantitative experiments on the PartNet-Mobility dataset demonstrate the effectiveness of our approach, achieving superior performance over previous methods.


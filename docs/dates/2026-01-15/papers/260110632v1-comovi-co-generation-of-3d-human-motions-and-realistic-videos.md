---
layout: default
title: CoMoVi: Co-Generation of 3D Human Motions and Realistic Videos
---

# CoMoVi: Co-Generation of 3D Human Motions and Realistic Videos
**arXiv**：[2601.10632v1](https://arxiv.org/abs/2601.10632) · [PDF](https://arxiv.org/pdf/2601.10632.pdf)  
**作者**：Chengfeng Zhao, Jiazhi Shu, Yubo Zhao, Tianyu Huang, Jiahao Lu, Zekai Gu, Chengwei Ren, Zhiyang Dou, Qing Shuai, Yuan Liu  

**一句话要点**：提出CoMoVi框架，通过耦合视频扩散模型同步生成3D人体动作与真实视频。

**关键词**：3D人体动作生成, 视频生成, 扩散模型, 协同生成, 数据集构建

## 3 点简述
- 核心问题：3D人体动作与2D视频生成过程内在耦合，需同步处理以提升一致性与泛化能力。
- 方法要点：设计双分支扩散模型，结合2D动作表示与3D-2D交叉注意力，实现动作与视频的协同生成。
- 实验或效果：构建大规模数据集CoMoVi Dataset，实验验证在3D动作与视频生成任务中的有效性。

## 摘要（原文）

> In this paper, we find that the generation of 3D human motions and 2D human videos is intrinsically coupled. 3D motions provide the structural prior for plausibility and consistency in videos, while pre-trained video models offer strong generalization capabilities for motions, which necessitate coupling their generation processes. Based on this, we present CoMoVi, a co-generative framework that couples two video diffusion models (VDMs) to generate 3D human motions and videos synchronously within a single diffusion denoising loop. To achieve this, we first propose an effective 2D human motion representation that can inherit the powerful prior of pre-trained VDMs. Then, we design a dual-branch diffusion model to couple human motion and video generation process with mutual feature interaction and 3D-2D cross attentions. Moreover, we curate CoMoVi Dataset, a large-scale real-world human video dataset with text and motion annotations, covering diverse and challenging human motions. Extensive experiments demonstrate the effectiveness of our method in both 3D human motion and video generation tasks.


---
layout: default
title: Instruction-Driven 3D Facial Expression Generation and Transition
---

# Instruction-Driven 3D Facial Expression Generation and Transition
**arXiv**：[2601.08179v1](https://arxiv.org/abs/2601.08179) · [PDF](https://arxiv.org/pdf/2601.08179.pdf)  
**作者**：Anh H. Vo, Tae-Seok Kim, Hulin Jin, Soo-Mi Choi, Yong-Guk Kim  

**一句话要点**：提出指令驱动的3D面部表情生成与过渡框架，以文本指令控制表情序列生成。

**关键词**：3D面部表情生成, 指令驱动模型, 表情过渡, 多模态学习, 语义理解

## 3 点简述
- 核心问题：3D虚拟角色通常只有六种基本表情，难以模拟真实情感变化和表情间平滑过渡。
- 方法要点：引入IFED模块学习文本与表情特征关联，结合I2FET方法优化语义理解，生成表情序列。
- 实验或效果：在CK+和CelebV-HQ数据集上优于现有方法，能根据文本指令生成表情轨迹。

## 摘要（原文）

> A 3D avatar typically has one of six cardinal facial expressions. To simulate realistic emotional variation, we should be able to render a facial transition between two arbitrary expressions. This study presents a new framework for instruction-driven facial expression generation that produces a 3D face and, starting from an image of the face, transforms the facial expression from one designated facial expression to another. The Instruction-driven Facial Expression Decomposer (IFED) module is introduced to facilitate multimodal data learning and capture the correlation between textual descriptions and facial expression features. Subsequently, we propose the Instruction to Facial Expression Transition (I2FET) method, which leverages IFED and a vertex reconstruction loss function to refine the semantic comprehension of latent vectors, thus generating a facial expression sequence according to the given instruction. Lastly, we present the Facial Expression Transition model to generate smooth transitions between facial expressions. Extensive evaluation suggests that the proposed model outperforms state-of-the-art methods on the CK+ and CelebV-HQ datasets. The results show that our framework can generate facial expression trajectories according to text instruction. Considering that text prompts allow us to make diverse descriptions of human emotional states, the repertoire of facial expressions and the transitions between them can be expanded greatly. We expect our framework to find various practical applications More information about our project can be found at https://vohoanganh.github.io/tg3dfet/


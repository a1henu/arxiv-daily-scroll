---
layout: default
title: SynHLMA:Synthesizing Hand Language Manipulation for Articulated Object with Discrete Human Object Interaction Representation
---

# SynHLMA:Synthesizing Hand Language Manipulation for Articulated Object with Discrete Human Object Interaction Representation
**arXiv**：[2510.25268v1](https://arxiv.org/abs/2510.25268) · [PDF](https://arxiv.org/pdf/2510.25268.pdf)  
**作者**：Wang zhi, Yuyan Liu, Liu Liu, Li Zhang, Ruixuan Lu, Dan Guo  

**一句话要点**：提出SynHLMA框架以合成手部语言操控铰接物体的交互序列

**关键词**：手部抓取合成, 铰接物体交互, 语言指令对齐, 离散表示学习, 机器人模仿学习

## 3 点简述
- 核心问题：铰接物体交互中，手部抓取需结合物体功能与长期变形序列
- 方法要点：使用离散HAOI表示和语言嵌入，训练模型对齐抓取过程与语言描述
- 实验或效果：在HAOI-lang数据集上优于现有方法，并应用于机器人抓取

## 摘要（原文）

> Generating hand grasps with language instructions is a widely studied topic
> that benefits from embodied AI and VR/AR applications. While transferring into
> hand articulatied object interaction (HAOI), the hand grasps synthesis requires
> not only object functionality but also long-term manipulation sequence along
> the object deformation. This paper proposes a novel HAOI sequence generation
> framework SynHLMA, to synthesize hand language manipulation for articulated
> objects. Given a complete point cloud of an articulated object, we utilize a
> discrete HAOI representation to model each hand object interaction frame. Along
> with the natural language embeddings, the representations are trained by an
> HAOI manipulation language model to align the grasping process with its
> language description in a shared representation space. A joint-aware loss is
> employed to ensure hand grasps follow the dynamic variations of articulated
> object joints. In this way, our SynHLMA achieves three typical hand
> manipulation tasks for articulated objects of HAOI generation, HAOI prediction
> and HAOI interpolation. We evaluate SynHLMA on our built HAOI-lang dataset and
> experimental results demonstrate the superior hand grasp sequence generation
> performance comparing with state-of-the-art. We also show a robotics grasp
> application that enables dexterous grasps execution from imitation learning
> using the manipulation sequence provided by our SynHLMA. Our codes and datasets
> will be made publicly available.


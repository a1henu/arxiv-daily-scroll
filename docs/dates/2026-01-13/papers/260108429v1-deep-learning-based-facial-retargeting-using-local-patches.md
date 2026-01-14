---
layout: default
title: Deep Learning Based Facial Retargeting Using Local Patches
---

# Deep Learning Based Facial Retargeting Using Local Patches
**arXiv**：[2601.08429v1](https://arxiv.org/abs/2601.08429) · [PDF](https://arxiv.org/pdf/2601.08429.pdf)  
**作者**：Yeonsoo Choi, Inyup Lee, Sihun Cha, Seonghyeon Kim, Sunjin Jung, Junyong Noh  

**一句话要点**：提出基于局部块的面部重定向方法，以解决风格化3D角色面部动画语义保持问题。

**关键词**：面部重定向, 局部块处理, 风格化角色, 语义保持, 深度学习

## 3 点简述
- 核心问题：风格化或夸张3D角色面部结构偏离人类，导致传统重定向方法难以保持原始面部运动的语义。
- 方法要点：通过自动提取源视频局部块、重演生成目标局部块，并估计动画参数，实现语义传递。
- 实验或效果：广泛实验表明，该方法能成功将源面部表情语义转移到面部特征比例变化大的风格化角色上。

## 摘要（原文）

> In the era of digital animation, the quest to produce lifelike facial animations for virtual characters has led to the development of various retargeting methods. While the retargeting facial motion between models of similar shapes has been very successful, challenges arise when the retargeting is performed on stylized or exaggerated 3D characters that deviate significantly from human facial structures. In this scenario, it is important to consider the target character's facial structure and possible range of motion to preserve the semantics assumed by the original facial motions after the retargeting. To achieve this, we propose a local patch-based retargeting method that transfers facial animations captured in a source performance video to a target stylized 3D character. Our method consists of three modules. The Automatic Patch Extraction Module extracts local patches from the source video frame. These patches are processed through the Reenactment Module to generate correspondingly re-enacted target local patches. The Weight Estimation Module calculates the animation parameters for the target character at every frame for the creation of a complete facial animation sequence. Extensive experiments demonstrate that our method can successfully transfer the semantic meaning of source facial expressions to stylized characters with considerable variations in facial feature proportion.


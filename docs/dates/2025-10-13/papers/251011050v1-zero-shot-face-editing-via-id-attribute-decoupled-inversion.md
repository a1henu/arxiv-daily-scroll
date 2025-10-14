---
layout: default
title: Zero-shot Face Editing via ID-Attribute Decoupled Inversion
---

# Zero-shot Face Editing via ID-Attribute Decoupled Inversion
**arXiv**：[2510.11050v1](https://arxiv.org/abs/2510.11050) · [PDF](https://arxiv.org/pdf/2510.11050.pdf)  
**作者**：Yang Hou, Minggu Wang, Jianjun Zhao  

**一句话要点**：提出ID-属性解耦反演方法以解决零样本人脸编辑中的ID和结构一致性问题

**关键词**：人脸编辑, 零样本学习, 扩散模型, ID保持, 属性操控

## 3 点简述
- 核心问题：文本引导扩散模型在真实人脸编辑中难以保持ID和结构一致性
- 方法要点：将人脸表示分解为ID和属性特征，作为联合条件指导反演和扩散过程
- 实验或效果：支持多属性编辑，仅需文本提示，保持ID并实现精确操控

## 摘要（原文）

> Recent advancements in text-guided diffusion models have shown promise for
> general image editing via inversion techniques, but often struggle to maintain
> ID and structural consistency in real face editing tasks. To address this
> limitation, we propose a zero-shot face editing method based on ID-Attribute
> Decoupled Inversion. Specifically, we decompose the face representation into ID
> and attribute features, using them as joint conditions to guide both the
> inversion and the reverse diffusion processes. This allows independent control
> over ID and attributes, ensuring strong ID preservation and structural
> consistency while enabling precise facial attribute manipulation. Our method
> supports a wide range of complex multi-attribute face editing tasks using only
> text prompts, without requiring region-specific input, and operates at a speed
> comparable to DDIM inversion. Comprehensive experiments demonstrate its
> practicality and effectiveness.


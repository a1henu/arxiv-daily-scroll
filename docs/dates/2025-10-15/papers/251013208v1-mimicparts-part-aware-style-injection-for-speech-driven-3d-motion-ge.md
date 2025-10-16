---
layout: default
title: MimicParts: Part-aware Style Injection for Speech-Driven 3D Motion Generation
---

# MimicParts: Part-aware Style Injection for Speech-Driven 3D Motion Generation
**arXiv**：[2510.13208v1](https://arxiv.org/abs/2510.13208) · [PDF](https://arxiv.org/pdf/2510.13208.pdf)  
**作者**：Lianlian Liu, YongKang He, Zhaojie Chu, Xiaofen Xing, Xiangmin Xu  

**一句话要点**：提出MimicParts框架以解决语音驱动3D运动生成中的风格多样性和区域差异问题

**关键词**：语音驱动运动生成, 3D人体动画, 风格注入, 区域感知, 去噪网络, 注意力机制

## 3 点简述
- 核心问题：现有方法简化风格多样性或忽略身体区域运动风格差异，限制运动真实感
- 方法要点：通过分区域风格注入和去噪网络，捕捉细粒度区域差异并动态适应语音节奏和情感
- 实验或效果：实验显示方法优于现有方法，生成更自然和富有表现力的3D人体运动序列

## 摘要（原文）

> Generating stylized 3D human motion from speech signals presents substantial
> challenges, primarily due to the intricate and fine-grained relationships among
> speech signals, individual styles, and the corresponding body movements.
> Current style encoding approaches either oversimplify stylistic diversity or
> ignore regional motion style differences (e.g., upper vs. lower body), limiting
> motion realism. Additionally, motion style should dynamically adapt to changes
> in speech rhythm and emotion, but existing methods often overlook this. To
> address these issues, we propose MimicParts, a novel framework designed to
> enhance stylized motion generation based on part-aware style injection and
> part-aware denoising network. It divides the body into different regions to
> encode localized motion styles, enabling the model to capture fine-grained
> regional differences. Furthermore, our part-aware attention block allows rhythm
> and emotion cues to guide each body region precisely, ensuring that the
> generated motion aligns with variations in speech rhythm and emotional state.
> Experimental results show that our method outperforming existing methods
> showcasing naturalness and expressive 3D human motion sequences.


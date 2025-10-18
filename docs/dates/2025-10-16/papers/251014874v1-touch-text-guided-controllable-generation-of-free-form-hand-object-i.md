---
layout: default
title: TOUCH: Text-guided Controllable Generation of Free-Form Hand-Object Interactions
---

# TOUCH: Text-guided Controllable Generation of Free-Form Hand-Object Interactions
**arXiv**：[2510.14874v1](https://arxiv.org/abs/2510.14874) · [PDF](https://arxiv.org/pdf/2510.14874.pdf)  
**作者**：Guangyi Han, Wei Zhai, Yuhang Yang, Yang Cao, Zheng-Jun Zha  

**一句话要点**：提出TOUCH框架以生成可控、多样且物理合理的手-物体自由交互。

**关键词**：手-物体交互生成, 自由形式交互, 多级扩散模型, 细粒度语义控制, 物理约束优化, WildO2数据集

## 3 点简述
- 现有手-物体交互生成局限于固定抓取模式，缺乏日常交互多样性。
- TOUCH使用多级扩散模型，结合细粒度语义控制，生成超越抓取的手势。
- 实验验证方法能生成可控、多样且物理合理的手交互，代表日常活动。

## 摘要（原文）

> Hand-object interaction (HOI) is fundamental for humans to express intent.
> Existing HOI generation research is predominantly confined to fixed grasping
> patterns, where control is tied to physical priors such as force closure or
> generic intent instructions, even when expressed through elaborate language.
> Such an overly general conditioning imposes a strong inductive bias for stable
> grasps, thus failing to capture the diversity of daily HOI. To address these
> limitations, we introduce Free-Form HOI Generation, which aims to generate
> controllable, diverse, and physically plausible HOI conditioned on fine-grained
> intent, extending HOI from grasping to free-form interactions, like pushing,
> poking, and rotating. To support this task, we construct WildO2, an in-the-wild
> diverse 3D HOI dataset, which includes diverse HOI derived from internet
> videos. Specifically, it contains 4.4k unique interactions across 92 intents
> and 610 object categories, each with detailed semantic annotations. Building on
> this dataset, we propose TOUCH, a three-stage framework centered on a
> multi-level diffusion model that facilitates fine-grained semantic control to
> generate versatile hand poses beyond grasping priors. This process leverages
> explicit contact modeling for conditioning and is subsequently refined with
> contact consistency and physical constraints to ensure realism. Comprehensive
> experiments demonstrate our method's ability to generate controllable, diverse,
> and physically plausible hand interactions representative of daily activities.
> The project page is $\href{https://guangyid.github.io/hoi123touch}{here}$.


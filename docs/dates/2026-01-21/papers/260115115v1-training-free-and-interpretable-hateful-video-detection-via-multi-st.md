---
layout: default
title: Training-Free and Interpretable Hateful Video Detection via Multi-stage Adversarial Reasoning
---

# Training-Free and Interpretable Hateful Video Detection via Multi-stage Adversarial Reasoning
**arXiv**：[2601.15115v1](https://arxiv.org/abs/2601.15115) · [PDF](https://arxiv.org/pdf/2601.15115.pdf)  
**作者**：Shuonan Yang, Yuchen Zhang, Zeyu Fu  

**一句话要点**：提出MARS框架，通过多阶段对抗推理实现无需训练且可解释的仇恨视频检测。

**关键词**：仇恨视频检测, 无需训练方法, 多阶段对抗推理, 可解释性, 视频内容分析

## 3 点简述
- 仇恨视频检测面临训练数据有限和缺乏可解释性的挑战。
- MARS采用多阶段对抗推理，包括客观描述、证据推理和反证据推理。
- 在两个真实数据集上，MARS在某些设置下优于其他无需训练方法，并在一个数据集上超越基于训练的方法。

## 摘要（原文）

> Hateful videos pose serious risks by amplifying discrimination, inciting violence, and undermining online safety. Existing training-based hateful video detection methods are constrained by limited training data and lack of interpretability, while directly prompting large vision-language models often struggle to deliver reliable hate detection. To address these challenges, this paper introduces MARS, a training-free Multi-stage Adversarial ReaSoning framework that enables reliable and interpretable hateful content detection. MARS begins with the objective description of video content, establishing a neutral foundation for subsequent analysis. Building on this, it develops evidence-based reasoning that supports potential hateful interpretations, while in parallel incorporating counter-evidence reasoning to capture plausible non-hateful perspectives. Finally, these perspectives are synthesized into a conclusive and explainable decision. Extensive evaluation on two real-world datasets shows that MARS achieves up to 10% improvement under certain backbones and settings compared to other training-free approaches and outperforms state-of-the-art training-based methods on one dataset. In addition, MARS produces human-understandable justifications, thereby supporting compliance oversight and enhancing the transparency of content moderation workflows. The code is available at https://github.com/Multimodal-Intelligence-Lab-MIL/MARS.


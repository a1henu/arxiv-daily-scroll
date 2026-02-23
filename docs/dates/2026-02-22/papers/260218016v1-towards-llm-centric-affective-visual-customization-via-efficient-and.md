---
layout: default
title: Towards LLM-centric Affective Visual Customization via Efficient and Precise Emotion Manipulating
---

# Towards LLM-centric Affective Visual Customization via Efficient and Precise Emotion Manipulating
**arXiv**：[2602.18016v1](https://arxiv.org/abs/2602.18016) · [PDF](https://arxiv.org/pdf/2602.18016.pdf)  
**作者**：Jiamin Luo, Xuqian Gu, Jingjing Wang, Jiahong Lu  

**一句话要点**：提出基于大语言模型的高效精准情感视觉定制方法，以解决图像情感编辑中的语义对齐与内容保留问题。

**关键词**：情感视觉定制, 大语言模型, 图像编辑, 语义对齐, 内容保留

## 3 点简述
- 核心问题：现有视觉定制方法忽视主观情感内容，缺乏通用基础模型进行情感视觉定制。
- 方法要点：设计高效情感语义转换模块和精准情感无关内容保留模块，实现图像情感编辑。
- 实验或效果：在构建的数据集上验证方法优于先进基线，证明情感信息的重要性和方法的有效性。

## 摘要（原文）

> Previous studies on visual customization primarily rely on the objective alignment between various control signals (e.g., language, layout and canny) and the edited images, which largely ignore the subjective emotional contents, and more importantly lack general-purpose foundation models for affective visual customization. With this in mind, this paper proposes an LLM-centric Affective Visual Customization (L-AVC) task, which focuses on generating images within modifying their subjective emotions via Multimodal LLM. Further, this paper contends that how to make the model efficiently align emotion conversion in semantics (named inter-emotion semantic conversion) and how to precisely retain emotion-agnostic contents (named exter-emotion semantic retaining) are rather important and challenging in this L-AVC task. To this end, this paper proposes an Efficient and Precise Emotion Manipulating approach for editing subjective emotions in images. Specifically, an Efficient Inter-emotion Converting (EIC) module is tailored to make the LLM efficiently align emotion conversion in semantics before and after editing, followed by a Precise Exter-emotion Retaining (PER) module to precisely retain the emotion-agnostic contents. Comprehensive experimental evaluations on our constructed L-AVC dataset demonstrate the great advantage of the proposed EPEM approach to the L-AVC task over several state-of-the-art baselines. This justifies the importance of emotion information for L-AVC and the effectiveness of EPEM in efficiently and precisely manipulating such information.


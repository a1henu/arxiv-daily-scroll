---
layout: default
title: Interaction-via-Actions: Cattle Interaction Detection with Joint Learning of Action-Interaction Latent Space
---

# Interaction-via-Actions: Cattle Interaction Detection with Joint Learning of Action-Interaction Latent Space
**arXiv**：[2512.16133v1](https://arxiv.org/abs/2512.16133) · [PDF](https://arxiv.org/pdf/2512.16133.pdf)  
**作者**：Ren Nakagawa, Yang Yang, Risa Shinoda, Hiroaki Santo, Kenji Oyama, Fumio Okura, Takenao Ohkawa  

**一句话要点**：提出CattleAct方法，通过动作-交互联合学习检测放牧牛群行为交互，用于智能畜牧管理。

**关键词**：行为交互检测, 潜在空间学习, 对比学习, 智能畜牧, 动作分解, 数据高效方法

## 3 点简述
- 核心问题：放牧牛群交互检测缺乏全面数据集，交互事件罕见，传统方法难以直接应用。
- 方法要点：从大规模动作数据学习动作潜在空间，通过对比学习微调嵌入罕见交互，构建统一动作-交互潜在空间。
- 实验或效果：在商业规模牧场实验中，相比基线方法实现更准确的交互检测，并集成视频与GPS开发实用系统。

## 摘要（原文）

> This paper introduces a method and application for automatically detecting behavioral interactions between grazing cattle from a single image, which is essential for smart livestock management in the cattle industry, such as for detecting estrus. Although interaction detection for humans has been actively studied, a non-trivial challenge lies in cattle interaction detection, specifically the lack of a comprehensive behavioral dataset that includes interactions, as the interactions of grazing cattle are rare events. We, therefore, propose CattleAct, a data-efficient method for interaction detection by decomposing interactions into the combinations of actions by individual cattle. Specifically, we first learn an action latent space from a large-scale cattle action dataset. Then, we embed rare interactions via the fine-tuning of the pre-trained latent space using contrastive learning, thereby constructing a unified latent space of actions and interactions. On top of the proposed method, we develop a practical working system integrating video and GPS inputs. Experiments on a commercial-scale pasture demonstrate the accurate interaction detection achieved by our method compared to the baselines. Our implementation is available at https://github.com/rakawanegan/CattleAct.


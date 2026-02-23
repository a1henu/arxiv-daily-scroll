---
layout: default
title: DeepSVU: Towards In-depth Security-oriented Video Understanding via Unified Physical-world Regularized MoE
---

# DeepSVU: Towards In-depth Security-oriented Video Understanding via Unified Physical-world Regularized MoE
**arXiv**：[2602.18019v1](https://arxiv.org/abs/2602.18019) · [PDF](https://arxiv.org/pdf/2602.18019.pdf)  
**作者**：Yujie Jin, Wenxin Zhang, Jingjing Wang, Guodong Zhou  

**一句话要点**：提出统一物理世界正则化MoE方法，以解决深度安全视频理解任务中的信息建模与权衡挑战。

**关键词**：安全视频理解, 混合专家模型, 物理世界建模, 视频-语言模型, 指令数据集

## 3 点简述
- 核心问题：现有安全视频理解任务缺乏对威胁原因生成与评估的能力，需建模从粗到细的物理世界信息。
- 方法要点：设计统一物理世界增强MoE块和物理世界权衡正则器，分别处理信息建模与自适应权衡。
- 实验或效果：在DeepSVU指令数据集上优于先进视频-LLM和非VLM方法，验证了物理世界信息的重要性。

## 摘要（原文）

> In the literature, prior research on Security-oriented Video Understanding (SVU) has predominantly focused on detecting and localize the threats (e.g., shootings, robberies) in videos, while largely lacking the effective capability to generate and evaluate the threat causes. Motivated by these gaps, this paper introduces a new chat paradigm SVU task, i.e., In-depth Security-oriented Video Understanding (DeepSVU), which aims to not only identify and locate the threats but also attribute and evaluate the causes threatening segments. Furthermore, this paper reveals two key challenges in the proposed task: 1) how to effectively model the coarse-to-fine physical-world information (e.g., human behavior, object interactions and background context) to boost the DeepSVU task; and 2) how to adaptively trade off these factors. To tackle these challenges, this paper proposes a new Unified Physical-world Regularized MoE (UPRM) approach. Specifically, UPRM incorporates two key components: the Unified Physical-world Enhanced MoE (UPE) Block and the Physical-world Trade-off Regularizer (PTR), to address the above two challenges, respectively. Extensive experiments conduct on our DeepSVU instructions datasets (i.e., UCF-C instructions and CUVA instructions) demonstrate that UPRM outperforms several advanced Video-LLMs as well as non-VLM approaches. Such information.These justify the importance of the coarse-to-fine physical-world information in the DeepSVU task and demonstrate the effectiveness of our UPRM in capturing such information.


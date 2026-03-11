---
layout: default
title: Does the Question Really Matter? Training-Free Data Selection for Vision-Language SFT
---

# Does the Question Really Matter? Training-Free Data Selection for Vision-Language SFT
**arXiv**：[2603.09715v1](https://arxiv.org/abs/2603.09715) · [PDF](https://arxiv.org/pdf/2603.09715.pdf)  
**作者**：Peng Sun, Huawen Shen, Yi Ban, Tianfan Fu, Yanbo Wang, Yuqiang Li  

**一句话要点**：提出CVS训练免费数据选择方法，以提升视觉语言大模型指令调优效果。

**关键词**：视觉语言大模型, 数据选择, 训练免费方法, 跨模态推理, 指令调优

## 3 点简述
- 核心问题：视觉指令调优中，许多样本依赖语言模式或常识捷径，缺乏真正跨模态推理，限制多模态学习效果。
- 方法要点：基于问题引入应显著改变模型对答案有效性的评估，利用冻结VLLM作为评估器，测量有无问题条件下答案有效性的差异，识别需视觉语言联合推理的样本。
- 实验或效果：在Vision-Flan和The Cauldron数据集上，CVS仅用10%和15%数据分别超越全数据训练3.5%和4.8%，并降低计算成本17.3%和44.4%。

## 摘要（原文）

> Visual instruction tuning is crucial for improving vision-language large models (VLLMs). However, many samples can be solved via linguistic patterns or common-sense shortcuts, without genuine cross-modal reasoning, limiting the effectiveness of multimodal learning. Prior data selection methods often rely on costly proxy model training and focus on difficulty or diversity, failing to capture a sample's true contribution to vision-language joint reasoning. In this paper, we propose CVS, a training-free data selection method based on the insight that, for high-quality multimodal samples, introducing the question should substantially alter the model's assessment of answer validity given an image. CVS leverages a frozen VLLM as an evaluator and measures the discrepancy in answer validity with and without conditioning on the question, enabling the identification of samples that require vision-language joint reasoning while filtering semantic-conflict noise. Experiments on Vision-Flan and The Cauldron show that CVS achieves solid performance across datasets. On Vision-Flan, CVS outperforms full-data training by 3.5% and 4.8% using only 10% and 15% of the data, respectively, and remains robust on the highly heterogeneous Cauldron dataset. Moreover, CVS reduces computational cost by 17.3% and 44.4% compared to COINCIDE and XMAS.


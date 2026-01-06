---
layout: default
title: DatBench: Discriminative, Faithful, and Efficient VLM Evaluations
---

# DatBench: Discriminative, Faithful, and Efficient VLM Evaluations
**arXiv**：[2601.02316v1](https://arxiv.org/abs/2601.02316) · [PDF](https://arxiv.org/pdf/2601.02316.pdf)  
**作者**：Siddharth Joshi, Haoli Yin, Rishabh Adiga, Ricardo Monti, Aldo Carranza, Alex Fang, Alvin Deng, Amro Abbas, Brett Larsen, Cody Blakeney, Darren Teh, David Schwab, Fan Pan, Haakon Mongstad, Jack Urbanek, Jason Lee, Jason Telanoff, Josh Wills, Kaleigh Mentzer, Luke Merrick, Parth Doshi, Paul Burstein, Pratyush Maini, Scott Loftin, Spandan Das, Tony Jiang, Vineeth Dorna, Zhengping Wang, Bogdan Gaza, Ari Morcos, Matthew Leavitt  

**一句话要点**：提出DatBench评估套件，通过转换和过滤提升视觉语言模型评估的忠实性、区分性和效率。

**关键词**：视觉语言模型评估, 评估数据集优化, 生成任务转换, 计算效率提升, 忠实性分析, 区分性改进

## 3 点简述
- 核心问题：现有VLM评估存在忠实性差、区分性低和计算成本高的问题，如多项选择题奖励猜测、可盲目解答样本占比高。
- 方法要点：通过将多项选择题转换为生成任务，并过滤盲目可解和错误标注样本，优化评估数据集。
- 实验或效果：发布DatBench-Full和DatBench，后者实现平均13倍加速，同时保持区分能力，揭示模型能力下降达35%。

## 摘要（原文）

> Empirical evaluation serves as the primary compass guiding research progress in foundation models. Despite a large body of work focused on training frontier vision-language models (VLMs), approaches to their evaluation remain nascent. To guide their maturation, we propose three desiderata that evaluations should satisfy: (1) faithfulness to the modality and application, (2) discriminability between models of varying quality, and (3) efficiency in compute. Through this lens, we identify critical failure modes that violate faithfulness and discriminability, misrepresenting model capabilities: (i) multiple-choice formats reward guessing, poorly reflect downstream use cases, and saturate early as models improve; (ii) blindly solvable questions, which can be answered without images, constitute up to 70% of some evaluations; and (iii) mislabeled or ambiguous samples compromise up to 42% of examples in certain datasets. Regarding efficiency, the computational burden of evaluating frontier models has become prohibitive: by some accounts, nearly 20% of development compute is devoted to evaluation alone. Rather than discarding existing benchmarks, we curate them via transformation and filtering to maximize fidelity and discriminability. We find that converting multiple-choice questions to generative tasks reveals sharp capability drops of up to 35%. In addition, filtering blindly solvable and mislabeled samples improves discriminative power while simultaneously reducing computational cost. We release DatBench-Full, a cleaned evaluation suite of 33 datasets spanning nine VLM capabilities, and DatBench, a discriminative subset that achieves 13x average speedup (up to 50x) while closely matching the discriminative power of the original datasets. Our work outlines a path toward evaluation practices that are both rigorous and sustainable as VLMs continue to scale.


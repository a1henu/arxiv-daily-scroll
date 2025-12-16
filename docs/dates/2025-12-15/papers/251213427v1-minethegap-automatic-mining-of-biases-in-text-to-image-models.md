---
layout: default
title: MineTheGap: Automatic Mining of Biases in Text-to-Image Models
---

# MineTheGap: Automatic Mining of Biases in Text-to-Image Models
**arXiv**：[2512.13427v1](https://arxiv.org/abs/2512.13427) · [PDF](https://arxiv.org/pdf/2512.13427.pdf)  
**作者**：Noa Cohen, Nurit Spingarn-Eliezer, Inbar Huberman-Spiegelglas, Tomer Michaeli  

**一句话要点**：提出MineTheGap方法，自动挖掘文本到图像模型的偏见提示

**关键词**：文本到图像模型, 偏见挖掘, 遗传算法, 偏见分数, 自动优化, 社会影响

## 3 点简述
- 核心问题：文本到图像模型在模糊提示下产生偏见，影响社会多样性和用户体验
- 方法要点：使用遗传算法迭代优化提示，基于新偏见分数比较图像与文本分布
- 实验或效果：在已知偏见数据集上验证偏见分数，提供代码和示例

## 摘要（原文）

> Text-to-Image (TTI) models generate images based on text prompts, which often leave certain aspects of the desired image ambiguous. When faced with these ambiguities, TTI models have been shown to exhibit biases in their interpretations. These biases can have societal impacts, e.g., when showing only a certain race for a stated occupation. They can also affect user experience when creating redundancy within a set of generated images instead of spanning diverse possibilities. Here, we introduce MineTheGap - a method for automatically mining prompts that cause a TTI model to generate biased outputs. Our method goes beyond merely detecting bias for a given prompt. Rather, it leverages a genetic algorithm to iteratively refine a pool of prompts, seeking for those that expose biases. This optimization process is driven by a novel bias score, which ranks biases according to their severity, as we validate on a dataset with known biases. For a given prompt, this score is obtained by comparing the distribution of generated images to the distribution of LLM-generated texts that constitute variations on the prompt. Code and examples are available on the project's webpage.


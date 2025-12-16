---
layout: default
title: From Zipf's Law to Neural Scaling through Heaps' Law and Hilberg's Hypothesis
---

# From Zipf's Law to Neural Scaling through Heaps' Law and Hilberg's Hypothesis
**arXiv**：[2512.13491v1](https://arxiv.org/abs/2512.13491) · [PDF](https://arxiv.org/pdf/2512.13491.pdf)  
**作者**：Łukasz Dębowski  

**一句话要点**：从Zipf定律推导神经缩放定律，揭示语言模型统计规律间的演绎联系

**关键词**：神经缩放定律, Zipf定律, Heaps定律, Hilberg假设, 基础模型, 统计语言学

## 3 点简述
- 核心问题：探究神经缩放定律与Zipf定律之间的演绎关系，解释基础模型性能随训练数据、参数和计算量变化的统计基础
- 方法要点：通过系统假设，从Zipf定律推导Heaps定律，再推导Hilberg假设，最终得出神经缩放定律
- 实验或效果：以Santa Fe过程为例，验证了四种统计定律的满足情况，支持理论推导

## 摘要（原文）

> We inspect the deductive connection between the neural scaling law and Zipf's law -- two statements discussed in machine learning and quantitative linguistics. The neural scaling law describes how the cross entropy rate of a foundation model -- such as a large language model -- changes with respect to the amount of training tokens, parameters, and compute. By contrast, Zipf's law posits that the distribution of tokens exhibits a power law tail. Whereas similar claims have been made in more specific settings, we show that the neural scaling law is a consequence of Zipf's law under certain broad assumptions that we reveal systematically. The derivation steps are as follows: We derive Heaps' law on the vocabulary growth from Zipf's law, Hilberg's hypothesis on the entropy scaling from Heaps' law, and the neural scaling from Hilberg's hypothesis. We illustrate these inference steps by a toy example of the Santa Fe process that satisfies all the four statistical laws.


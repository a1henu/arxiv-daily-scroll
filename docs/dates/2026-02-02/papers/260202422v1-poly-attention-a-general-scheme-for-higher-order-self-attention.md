---
layout: default
title: Poly-attention: a general scheme for higher-order self-attention
---

# Poly-attention: a general scheme for higher-order self-attention
**arXiv**：[2602.02422v1](https://arxiv.org/abs/2602.02422) · [PDF](https://arxiv.org/pdf/2602.02422.pdf)  
**作者**：Sayak Chakrabarti, Toniann Pitassi, Josh Alman  

**一句话要点**：提出Poly-attention机制以解决Transformer自注意力无法处理高阶相关任务的问题

**关键词**：自注意力机制, 高阶注意力, 计算复杂性, Transformer模型, 张量计算

## 3 点简述
- 核心问题：自注意力机制无法有效建模三元及以上相关标记或组合任务
- 方法要点：定义广义高阶自注意力类，支持任意高阶张量计算和标记关系结构
- 实验或效果：系统分析计算复杂性和表示能力，给出新算法和紧致下界

## 摘要（原文）

> The self-attention mechanism, at the heart of the Transformer model, is able to effectively model pairwise interactions between tokens. However, numerous recent works have shown that it is unable to perform basic tasks involving detecting triples of correlated tokens, or compositional tasks where multiple input tokens need to be referenced to generate a result. Some higher-dimensional alternatives to self-attention have been proposed to address this, including higher-order attention and Strassen attention, which can perform some of these polyadic tasks in exchange for slower, superquadratic running times.
>   In this work, we define a vast class of generalizations of self-attention, which we call poly-attention mechanisms. Our mechanisms can incorporate arbitrary higher-order (tensor) computations as well as arbitrary relationship structures between the input tokens, and they include the aforementioned alternatives as special cases. We then systematically study their computational complexity and representational strength, including giving new algorithms and matching complexity-theoretic lower bounds on the time complexity of computing the attention matrix exactly as well as approximately, and tightly determining which polyadic tasks they can each perform. Our results give interesting trade-offs between different desiderata for these mechanisms, including a tight relationship between how expressive a mechanism is, and how large the coefficients in the model may be so that the mechanism can be approximated in almost-linear time.
>   Notably, we give a new attention mechanism which can be computed exactly in quadratic time, and which can perform function composition for any fixed number of functions. Prior mechanisms, even for just composing two functions, could only be computed in superquadratic time, and our new lower bounds show that faster algorithms for them are not possible.


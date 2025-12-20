---
layout: default
title: Prefix Probing: Lightweight Harmful Content Detection for Large Language Models
---

# Prefix Probing: Lightweight Harmful Content Detection for Large Language Models
**arXiv**：[2512.16650v1](https://arxiv.org/abs/2512.16650) · [PDF](https://arxiv.org/pdf/2512.16650.pdf)  
**作者**：Jirui Yang, Hengqi Guo, Zhihui Lu, Yi Zhao, Yuansen Zhang, Shijing Hu, Qiang Duan, Yinggui Wang, Tao Wei  

**一句话要点**：提出Prefix Probing方法，通过前缀概率比较实现轻量级有害内容检测，以解决大语言模型在安全应用中的精度、延迟与成本权衡问题。

**关键词**：有害内容检测, 前缀探测, 大语言模型安全, 黑盒检测, 前缀缓存, 轻量级推理

## 3 点简述
- 核心问题：大语言模型在安全敏感应用中面临检测精度、推理延迟和部署成本的三方权衡。
- 方法要点：基于黑盒检测，比较“同意/执行”与“拒绝/安全”前缀的条件对数概率，利用前缀缓存降低开销至接近首词延迟。
- 实验或效果：实验显示检测效果与主流外部安全模型相当，计算成本极低且无需额外模型部署，实用性强。

## 摘要（原文）

> Large language models often face a three-way trade-off among detection accuracy, inference latency, and deployment cost when used in real-world safety-sensitive applications. This paper introduces Prefix Probing, a black-box harmful content detection method that compares the conditional log-probabilities of "agreement/execution" versus "refusal/safety" opening prefixes and leverages prefix caching to reduce detection overhead to near first-token latency. During inference, the method requires only a single log-probability computation over the probe prefixes to produce a harmfulness score and apply a threshold, without invoking any additional models or multi-stage inference. To further enhance the discriminative power of the prefixes, we design an efficient prefix construction algorithm that automatically discovers highly informative prefixes, substantially improving detection performance. Extensive experiments demonstrate that Prefix Probing achieves detection effectiveness comparable to mainstream external safety models while incurring only minimal computational cost and requiring no extra model deployment, highlighting its strong practicality and efficiency.


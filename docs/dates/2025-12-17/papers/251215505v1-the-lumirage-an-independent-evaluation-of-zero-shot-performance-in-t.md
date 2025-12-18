---
layout: default
title: The LUMirage: An independent evaluation of zero-shot performance in the LUMIR challenge
---

# The LUMirage: An independent evaluation of zero-shot performance in the LUMIR challenge
**arXiv**：[2512.15505v1](https://arxiv.org/abs/2512.15505) · [PDF](https://arxiv.org/pdf/2512.15505.pdf)  
**作者**：Rohit Jena, Pratik Chaudhari, James C. Gee  

**一句话要点**：独立评估LUMIR挑战中零样本性能，揭示深度学习在域外数据上的局限性

**关键词**：可变形图像配准, 零样本泛化, 域偏移, 神经影像, 深度学习评估, 临床工作流

## 3 点简述
- 核心问题：评估深度学习在LUMIR挑战中声称的零样本泛化能力，质疑其与域偏移理论的矛盾
- 方法要点：采用严格评估协议，独立重新测试不同对比度和分辨率的神经影像数据
- 实验或效果：发现深度学习在域外对比度上性能显著下降，高分辨率数据上存在可扩展性限制

## 摘要（原文）

> The LUMIR challenge represents an important benchmark for evaluating deformable image registration methods on large-scale neuroimaging data. While the challenge demonstrates that modern deep learning methods achieve competitive accuracy on T1-weighted MRI, it also claims exceptional zero-shot generalization to unseen contrasts and resolutions, assertions that contradict established understanding of domain shift in deep learning. In this paper, we perform an independent re-evaluation of these zero-shot claims using rigorous evaluation protocols while addressing potential sources of instrumentation bias. Our findings reveal a more nuanced picture: (1) deep learning methods perform comparably to iterative optimization on in-distribution T1w images and even on human-adjacent species (macaque), demonstrating improved task understanding; (2) however, performance degrades significantly on out-of-distribution contrasts (T2, T2*, FLAIR), with Cohen's d scores ranging from 0.7-1.5, indicating substantial practical impact on downstream clinical workflows; (3) deep learning methods face scalability limitations on high-resolution data, failing to run on 0.6 mm isotropic images, while iterative methods benefit from increased resolution; and (4) deep methods exhibit high sensitivity to preprocessing choices. These results align with the well-established literature on domain shift and suggest that claims of universal zero-shot superiority require careful scrutiny. We advocate for evaluation protocols that reflect practical clinical and research workflows rather than conditions that may inadvertently favor particular method classes.


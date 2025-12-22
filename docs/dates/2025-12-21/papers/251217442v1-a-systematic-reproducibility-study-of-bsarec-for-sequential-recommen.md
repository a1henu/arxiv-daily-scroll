---
layout: default
title: A Systematic Reproducibility Study of BSARec for Sequential Recommendation
---

# A Systematic Reproducibility Study of BSARec for Sequential Recommendation
**arXiv**：[2512.17442v1](https://arxiv.org/abs/2512.17442) · [PDF](https://arxiv.org/pdf/2512.17442.pdf)  
**作者**：Jan Hutter, Hua Chang Bakker, Stan Fris, Madelon Bernardy, Yuanna Liu  

**一句话要点**：系统复现BSARec并评估其频率增强组件在序列推荐中的有效性

**关键词**：序列推荐, 频率增强, Transformer, 傅里叶变换, 复现研究, 数字信号处理

## 3 点简述
- 核心问题：Transformer自注意力机制在序列推荐中作为低通滤波器，难以捕捉反映短期兴趣的高频信号
- 方法要点：BSARec通过傅里叶变换的频率层增强Transformer，但各组件效果未经验证
- 实验或效果：复现显示BSARec部分数据集表现更优，但数字信号处理方法相比残差连接无明显优势

## 摘要（原文）

> In sequential recommendation (SR), the self-attention mechanism of Transformer-based models acts as a low-pass filter, limiting their ability to capture high-frequency signals that reflect short-term user interests. To overcome this, BSARec augments the Transformer encoder with a frequency layer that rescales high-frequency components using the Fourier transform. However, the overall effectiveness of BSARec and the roles of its individual components have yet to be systematically validated. We reproduce BSARec and show that it outperforms other SR methods on some datasets. To empirically assess whether BSARec improves performance on high-frequency signals, we propose a metric to quantify user history frequency and evaluate SR methods across different user groups. We compare digital signal processing (DSP) techniques and find that the discrete wavelet transform (DWT) offer only slight improvements over Fourier transforms, and DSP methods provide no clear advantage over simple residual connections. Finally, we explore padding strategies and find that non-constant padding significantly improves recommendation performance, whereas constant padding hinders the frequency rescaler's ability to capture high-frequency signals.


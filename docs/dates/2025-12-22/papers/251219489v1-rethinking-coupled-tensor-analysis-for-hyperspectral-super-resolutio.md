---
layout: default
title: Rethinking Coupled Tensor Analysis for Hyperspectral Super-Resolution: Recoverable Modeling Under Endmember Variability
---

# Rethinking Coupled Tensor Analysis for Hyperspectral Super-Resolution: Recoverable Modeling Under Endmember Variability
**arXiv**：[2512.19489v1](https://arxiv.org/abs/2512.19489) · [PDF](https://arxiv.org/pdf/2512.19489.pdf)  
**作者**：Meng Ding, Xiao Fu  

**一句话要点**：提出LMN张量分解模型以解决高光谱超分辨率中的端元变异性问题

**关键词**：高光谱超分辨率, 耦合张量分解, 端元变异性, LMN模型, 恢复性理论

## 3 点简述
- 核心问题：现有耦合张量分解方法在端元变异性下缺乏物理可解释性和恢复性保证
- 方法要点：引入更灵活的LMN模型，平衡表达能力和可解释性，并建立恢复性理论
- 实验或效果：在合成和真实数据集上验证了方法的有效性和鲁棒性，优于现有方法

## 摘要（原文）

> This work revisits the hyperspectral super-resolution (HSR) problem, i.e., fusing a pair of spatially co-registered hyperspectral (HSI) and multispectral (MSI) images to recover a super-resolution image (SRI) that enhances the spatial resolution of the HSI. Coupled tensor decomposition (CTD)-based methods have gained traction in this domain, offering recoverability guarantees under various assumptions. Existing models such as canonical polyadic decomposition (CPD) and Tucker decomposition provide strong expressive power but lack physical interpretability. The block-term decomposition model with rank-$(L_r, L_r, 1)$ terms (the LL1 model) yields interpretable factors under the linear mixture model (LMM) of spectral images, but LMM assumptions are often violated in practice -- primarily due to nonlinear effects such as endmember variability (EV). To address this, we propose modeling spectral images using a more flexible block-term tensor decomposition with rank-$(L_r, M_r, N_r)$ terms (the LMN model). This modeling choice retains interpretability, subsumes CPD, Tucker, and LL1 as special cases, and robustly accounts for non-ideal effects such as EV, offering a balanced tradeoff between expressiveness and interpretability for HSR. Importantly, under the LMN model for HSI and MSI, recoverability of the SRI can still be established under proper conditions -- providing strong theoretical support. Extensive experiments on synthetic and real datasets further validate the effectiveness and robustness of the proposed method compared with existing CTD-based approaches.


---
layout: default
title: AI-Driven Structure Refinement of X-ray Diffraction
---

# AI-Driven Structure Refinement of X-ray Diffraction
**arXiv**：[2602.16372v1](https://arxiv.org/abs/2602.16372) · [PDF](https://arxiv.org/pdf/2602.16372.pdf)  
**作者**：Bin Cao, Qian Zhang, Zhenjie Feng, Taolue Zhang, Jiaqiang Huang, Lu-Tao Weng, Tong-Yi Zhang  

**一句话要点**：提出WPEM工作流，通过物理约束全谱分解解决X射线衍射重叠峰强度分配不稳定问题

**关键词**：X射线衍射精修, 全谱分解, 物理约束优化, 重叠峰处理, 多相材料分析, 布拉格一致性

## 3 点简述
- 核心问题：AI生成的XRD候选结构在下游精修中因重叠峰强度分配不稳定和衍射一致性弱而失败
- 方法要点：WPEM将布拉格定律作为显式约束，在批处理期望最大化框架中建模全谱为概率混合密度，迭代推断组分强度
- 实验或效果：在标准参考图案和多种实验场景中，WPEM相比FullProf和TOPAS产生更低的Rp/Rwp，实现稳定精修

## 摘要（原文）

> Artificial intelligence can rapidly propose candidate phases and structures from X-ray diffraction (XRD), but these hypotheses often fail in downstream refinement because peak intensities cannot be stably assigned under severe overlap and diffraction consistency is enforced only weakly. Here we introduce WPEM, a physics-constrained whole-pattern decomposition and refinement workflow that turns Bragg's law into an explicit constraint within a batch expectation--maximization framework. WPEM models the full profile as a probabilistic mixture density and iteratively infers component-resolved intensities while keeping peak centres Bragg-consistent, producing a continuous, physically admissible intensity representation that remains stable in heavily overlapped regions and in the presence of mixed radiation or multiple phases. We benchmark WPEM on standard reference patterns (\ce{PbSO4} and \ce{Tb2BaCoO5}), where it yields lower $R_{\mathrm{p}}$/$R_{\mathrm{wp}}$ than widely used packages (FullProf and TOPAS) under matched refinement conditions. We further demonstrate generality across realistic experimental scenarios, including phase-resolved decomposition of a multiphase Ti--15Nb thin film, quantitative recovery of \ce{NaCl}--\ce{Li2CO3} mixture compositions, separation of crystalline peaks from amorphous halos in semicrystalline polymers, high-throughput operando lattice tracking in layered cathodes, automated refinement of a compositionally disordered Ru--Mn oxide solid solution (CCDC 2530452), and quantitative phase-resolved deciphering of an ancient Egyptian make-up sample from synchrotron powder XRD. By providing Bragg-consistent, uncertainty-aware intensity partitioning as a refinement-ready interface, WPEM closes the gap between AI-generated hypotheses and diffraction-admissible structure refinement on challenging XRD data.


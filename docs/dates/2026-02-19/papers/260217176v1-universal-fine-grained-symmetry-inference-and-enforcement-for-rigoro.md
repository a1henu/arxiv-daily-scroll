---
layout: default
title: Universal Fine-Grained Symmetry Inference and Enforcement for Rigorous Crystal Structure Prediction
---

# Universal Fine-Grained Symmetry Inference and Enforcement for Rigorous Crystal Structure Prediction
**arXiv**：[2602.17176v1](https://arxiv.org/abs/2602.17176) · [PDF](https://arxiv.org/pdf/2602.17176.pdf)  
**作者**：Shi Yin, Jinming Mu, Xudong Zhu, Lixin He  

**一句话要点**：提出基于大语言模型和约束优化的通用细粒度对称性推断与执行框架，以严格预测晶体结构

**关键词**：晶体结构预测, 大语言模型, 对称性推断, 约束优化, 扩散模型, 材料发现

## 3 点简述
- 现有晶体结构预测方法依赖已知结构模板，限制物理保真度和新材料发现能力
- 利用大语言模型编码化学语义直接生成细粒度Wyckoff模式，结合约束优化确保代数一致性
- 在稳定性、唯一性和新颖性基准测试中达到先进性能，支持高效探索未知材料空间

## 摘要（原文）

> Crystal structure prediction (CSP), which aims to predict the three-dimensional atomic arrangement of a crystal from its composition, is central to materials discovery and mechanistic understanding. Existing deep learning models often treat crystallographic symmetry only as a soft heuristic or rely on space group and Wyckoff templates retrieved from known structures, which limits both physical fidelity and the ability to discover genuinely new material structures. In contrast to retrieval-based methods, our approach leverages large language models to encode chemical semantics and directly generate fine-grained Wyckoff patterns from composition, effectively circumventing the limitations inherent to database lookups. Crucially, we incorporate domain knowledge into the generative process through an efficient constrained-optimization search that rigorously enforces algebraic consistency between site multiplicities and atomic stoichiometry. By integrating this symmetry-consistent template into a diffusion backbone, our approach constrains the stochastic generative trajectory to a physically valid geometric manifold. This framework achieves state-of-the-art performance across stability, uniqueness, and novelty (SUN) benchmarks, alongside superior matching performance, thereby establishing a new paradigm for the rigorous exploration of targeted crystallographic space. This framework enables efficient expansion into previously uncharted materials space, eliminating reliance on existing databases or a priori structural knowledge.


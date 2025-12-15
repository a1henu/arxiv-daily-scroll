---
layout: default
title: QGEC : Quantum Golay Code Error Correction
---

# QGEC : Quantum Golay Code Error Correction
**arXiv**：[2512.11307v1](https://arxiv.org/abs/2512.11307) · [PDF](https://arxiv.org/pdf/2512.11307.pdf)  
**作者**：Hideo Mukai, Hoshitaro Ohnishi  

**一句话要点**：提出基于Golay码的量子纠错方法QGEC，利用Transformer解码提升容错量子计算效率

**关键词**：量子纠错, Golay码, Transformer解码, 噪声模型, 容错量子计算

## 3 点简述
- 量子纠错是量子计算的关键，需通过稳定子测量预测错误而非直接测量数据量子比特
- QGEC采用经典信息论中高效的Golay码，结合Transformer进行解码计算，评估不同噪声模型和权重集下的解码精度
- 实验表明，Golay码（23数据量子比特，码距7）比toric码（50数据量子比特，码距5）解码精度更高，可能更高效实现容错量子计算

## 摘要（原文）

> Quantum computers have the possibility of a much reduced calculation load compared with classical computers in specific problems. Quantum error correction (QEC) is vital for handling qubits, which are vulnerable to external noise. In QEC, actual errors are predicted from the results of syndrome measurements by stabilizer generators, in place of making direct measurements of the data qubits. Here, we propose Quantum Golay code Error Correction (QGEC), a QEC method using Golay code, which is an efficient coding method in classical information theory. We investigated our method's ability in decoding calculations with the Transformer. We evaluated the accuracy of the decoder in a code space defined by the generative polynomials with three different weights sets and three noise models with different correlations of bit-flip error and phase-flip error. Furthermore, under a noise model following a discrete uniform distribution, we compared the decoding performance of Transformer decoders with identical architectures trained respectively on Golay and toric codes. The results showed that the noise model with the smaller correlation gave better accuracy, while the weights of the generative polynomials had little effect on the accuracy of the decoder. In addition, they showed that Golay code requiring 23 data qubits and having a code distance of 7 achieved higher decoding accuracy than toric code which requiring 50 data qubits and having a code distance of 5. This suggests that implementing quantum error correction using a Transformer may enable the Golay code to realize fault-tolerant quantum computation more efficiently.


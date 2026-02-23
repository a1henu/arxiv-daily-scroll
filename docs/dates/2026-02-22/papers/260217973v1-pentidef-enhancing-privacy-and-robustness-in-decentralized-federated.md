---
layout: default
title: PenTiDef: Enhancing Privacy and Robustness in Decentralized Federated Intrusion Detection Systems against Poisoning Attacks
---

# PenTiDef: Enhancing Privacy and Robustness in Decentralized Federated Intrusion Detection Systems against Poisoning Attacks
**arXiv**：[2602.17973v1](https://arxiv.org/abs/2602.17973) · [PDF](https://arxiv.org/pdf/2602.17973.pdf)  
**作者**：Phan The Duy, Nghi Hoang Khoa, Nguyen Tran Anh Quan, Luong Ha Tien, Ngo Duc Hoang Son, Van-Hau Pham  

**一句话要点**：提出PenTiDef框架以增强去中心化联邦入侵检测系统的隐私与抗毒化攻击鲁棒性

**关键词**：去中心化联邦学习, 入侵检测系统, 隐私保护, 毒化攻击防御, 区块链协调, 潜在空间表示

## 3 点简述
- 核心问题：去中心化联邦入侵检测系统面临数据隐私、中心协调缺失和毒化攻击脆弱性挑战
- 方法要点：结合分布式差分隐私保护数据，利用潜在空间表示检测恶意更新，并采用区块链协调机制
- 实验或效果：在CIC-IDS2018和Edge-IIoTSet数据集上优于现有防御方法，验证了框架的有效性

## 摘要（原文）

> The increasing deployment of Federated Learning (FL) in Intrusion Detection Systems (IDS) introduces new challenges related to data privacy, centralized coordination, and susceptibility to poisoning attacks. While significant research has focused on protecting traditional FL-IDS with centralized aggregation servers, there remains a notable gap in addressing the unique challenges of decentralized FL-IDS (DFL-IDS). This study aims to address the limitations of traditional centralized FL-IDS by proposing a novel defense framework tailored for the decentralized FL-IDS architecture, with a focus on privacy preservation and robustness against poisoning attacks. We propose PenTiDef, a privacy-preserving and robust defense framework for DFL-IDS, which incorporates Distributed Differential Privacy (DDP) to protect data confidentiality and utilizes latent space representations (LSR) derived from neural networks to detect malicious updates in the decentralized model aggregation context. To eliminate single points of failure and enhance trust without a centralized aggregation server, PenTiDef employs a blockchain-based decentralized coordination mechanism that manages model aggregation, tracks update history, and supports trust enforcement through smart contracts. Experimental results on CIC-IDS2018 and Edge-IIoTSet demonstrate that PenTiDef consistently outperforms existing defenses (e.g., FLARE, FedCC) across various attack scenarios and data distributions. These findings highlight the potential of PenTiDef as a scalable and secure framework for deploying DFL-based IDS in adversarial environments. By leveraging privacy protection, malicious behavior detection in hidden data, and working without a central server, it provides a useful security solution against real-world attacks from untrust participants.

